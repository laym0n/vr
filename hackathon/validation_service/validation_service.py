from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import httpx
from jsonschema import validate, ValidationError

app = FastAPI(
    title="Request Validator",
    root_path = "/api-gateway/validation-service",
    swagger_ui_parameters = {"openapiUrl": "/api-gateway/validation-service/openapi.json"}
)

# In-memory storage for the schema
result_schema: Optional[Dict[str, Any]] = None

# URL of the Generate-Schema microservice
GENERATE_SCHEMA_URL = "http://generate-schema-service:8000/generate-schema"  # Update the URL as needed


class ValidationRequest(BaseModel):
    ready_schema: Dict[str, Any]
    request_data: Dict[str, Any]


@app.post("/validate-request")
async def validate_request(validation_request: ValidationRequest):
    """
    Validate a request against a dynamically generated OpenAPI schema.
    """
    global result_schema

    # Step 1: Forward the request and schema to the Generate-Schema microservice
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GENERATE_SCHEMA_URL,
                json={
                    "ready_schema": validation_request.ready_schema,
                    "request_data": validation_request.request_data,
                },
            )
        response.raise_for_status()
        result_schema = response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Generate-Schema service: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"Generate-Schema service returned an error: {e.response.content}")

    # Step 2: Validate the request against the generated schema
    try:
        if result_schema and "paths" in result_schema:
            for path, methods in result_schema["paths"].items():
                for method, operation in methods.items():
                    if "requestBody" in operation:
                        schema = operation["requestBody"]["content"]["application/json"]["schema"]
                        validate(instance=validation_request.request_data, schema=schema)
        else:
            raise HTTPException(status_code=500, detail="Generated schema is missing required information.")
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Validation failed: {e.message}")

    return JSONResponse(content={"message": "Request is valid."})


@app.get("/schema")
async def get_saved_schema():
    """
    Get the currently saved schema.
    """
    if result_schema is None:
        raise HTTPException(status_code=404, detail="No schema saved yet.")
    return result_schema
