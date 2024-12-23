from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from typing import Dict

from starlette.requests import Request

app = FastAPI(title="Response Cacher",
              openapi_url="/api-gateway/cache-service/openapi.json",  # Путь для схемы OpenAPI
              swagger_ui_parameters={"openapiUrl": "/api-gateway/cache-service/openapi.json"}
)


# In-memory cache for storing responses
response_cache: Dict[str, Dict] = {}

class CacheRequest(BaseModel):
    idempotentKey: str
    response: Dict

class GetResponseRequest(BaseModel):
    idempotentKey: str

@app.post("/cache-response")
async def cache_response(request: CacheRequest):
    """
    Save a response in the cache with an idempotentKey.
    """
    if request.idempotentKey in response_cache:
        # If the key already exists, overwrite behavior is idempotent
        return {"message": "Response already exists. Returning existing response."}

    # Save the response
    response_cache[request.idempotentKey] = request.response
    return {"message": "Response cached successfully."}

@app.get("/get-response")
async def get_response(idempotentKey: str):
    """
    Retrieve a cached response using an idempotentKey.
    """
    response = response_cache.get(idempotentKey)
    if response is None:
        raise HTTPException(status_code=404, detail="Response not found for the given idempotentKey.")
    return {"response": response}
