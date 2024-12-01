from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from typing import Any, Dict

app = FastAPI(title="Request Distributor")

# Microservice URLs
VALIDATOR_URL = "http://request-validator-service:8001/validate-request"
CACHE_URL = "http://response-cacher-service:8002"
API_GATEWAY_URL = "http://api-gateway-service:8003"

# Request model
class DistributorRequest(BaseModel):
    request: Dict[str, Any]  # The incoming request from the client

@app.post("/distribute-request")
async def distribute_request(request_body: DistributorRequest):
    """
    Distribute a request: Validate it, check cache, or forward to the API Gateway.
    """
    request_data = request_body.request
    idempotent_key = str(hash(frozenset(request_data.items())))  # Generate a unique key based on the request

    # Step 1: Validate the request
    validation_payload = {"ready_schema": {}, "request_data": request_data}  # Empty schema for demo
    try:
        async with httpx.AsyncClient() as client:
            validation_response = await client.post(f"{VALIDATOR_URL}", json=validation_payload)
            validation_response.raise_for_status()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Request Validator: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=400, detail=f"Validation failed: {e.response.json()}")

    # Step 2: Check if the response is cached
    try:
        async with httpx.AsyncClient() as client:
            cache_response = await client.get(f"{CACHE_URL}/get-response", params={"idempotentKey": idempotent_key})
            if cache_response.status_code == 200:
                cached_response = cache_response.json()
                return {"source": "cache", "response": cached_response["response"]}
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Response Cacher: {e}")
    except httpx.HTTPStatusError:
        # cache miss, continue to original service
        pass

    # Step 3: Forward the request to the original service (API Gateway)
    try:
        async with httpx.AsyncClient() as client:
            original_service_response = await client.post(f"{API_GATEWAY_URL}", json=request_data)
            original_service_response.raise_for_status()
            original_response_data = original_service_response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting API Gateway: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"API Gateway returned an error: {e.response.json()}")

    # Step 4: Save the response in the cache
    cache_payload = {"idempotentKey": idempotent_key, "response": original_response_data}
    try:
        async with httpx.AsyncClient() as client:
            cache_save_response = await client.post(f"{CACHE_URL}/cache-response", json=cache_payload)
            cache_save_response.raise_for_status()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error saving response in cache: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"Cache service returned an error: {e.response.json()}")

    # Step 5: Return the original service response
    return {"source": "api-gateway", "response": original_response_data}
