from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="Response Cacher",
    root_path="/api-gateway/cache-service",
    swagger_ui_parameters={"openapiUrl": "/api-gateway/cache-service/openapi.json"}
)

# In-memory cache for storing responses
response_cache: Dict[str, str] = {}

class CacheRequest(BaseModel):
    idempotentKey: str
    response: Dict

@app.post("/cache")
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

@app.get("/cache/{idempotencyKey}")
async def get_cached_response(idempotencyKey: str):
    """
    Retrieve a cached response by idempotencyKey.
    """
    response = response_cache.get(idempotencyKey)
    if response is None:
        raise HTTPException(status_code=404, detail="Response not found for the given idempotencyKey.")
    return {"response": response}

@app.post("/cache/invalidate/{idempotencyKey}")
async def invalidate_cache(idempotencyKey: str):
    """
    Invalidate a specific cached response by idempotencyKey.
    """
    if idempotencyKey in response_cache:
        del response_cache[idempotencyKey]
        return {"message": f"Cache entry with idempotencyKey '{idempotencyKey}' invalidated successfully."}
    raise HTTPException(status_code=404, detail="Response not found for the given idempotencyKey.")
