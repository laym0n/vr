from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="OpenAPI Schema Generator",
    root_path="/api-gateway/generate-schema-service",
    swagger_ui_parameters={"openapiUrl": "/api-gateway/generate-schema-service/openapi.json"}
)

class SchemaResponse(BaseModel):
    openapi: str
    info: Dict[str, Any]
    paths: Dict[str, Any]

@app.post("/generate-schema", response_model=SchemaResponse)
async def generate_schema_endpoint(request: Request, ready_schema: Dict[str, Any]):
    """
    Generate and merge OpenAPI schema based on the incoming HTTP request and a ready schema.
    """
    # Parse the request and generate a schema
    generated_schema = await generate_schema(request)
    
    # Merge generated schema with the ready schema
    merged_schema = merge_schemas(ready_schema, generated_schema)
    
    return merged_schema

async def generate_schema(request: Request) -> Dict[str, Any]:
    """
    Generate an OpenAPI schema based on the incoming HTTP request.
    :param request: The HTTP request object.
    :return: Generated OpenAPI schema as a dictionary.
    """
    # Extract method and path from the request
    method = request.method.lower()
    url_path = str(request.url.path)

    # Extract headers
    headers = {key: value for key, value in request.headers.items()}

    # Extract query parameters
    query_params = {key: value for key, value in request.query_params.items()}

    # Extract body (if any)
    body = {}
    if "application/json" in headers.get("content-type", ""):
        body = await request.json()

    # Construct a basic OpenAPI schema
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Generated API",
            "version": "1.0.0",
        },
        "paths": {
            url_path: {
                method: {
                    "summary": f"Auto-generated operation for {method.upper()} {url_path}",
                    "description": "This endpoint was dynamically generated based on the request.",
                    "parameters": [
                        {
                            "name": param,
                            "in": "query",
                            "required": False,
                            "schema": {"type": "string"},
                        }
                        for param in query_params.keys()
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "properties": {key: {"type": "string"} for key in body.keys()}}
                            }
                        }
                    } if body else {},
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object", "properties": {"message": {"type": "string"}}}
                                }
                            },
                        }
                    },
                }
            }
        },
    }
    return schema

def merge_schemas(ready_schema: Dict[str, Any], new_schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge a ready OpenAPI schema with a newly generated schema.
    :param ready_schema: The pre-existing OpenAPI schema.
    :param new_schema: The newly generated OpenAPI schema.
    :return: Merged OpenAPI schema.
    """
    # Ensure both schemas use the same OpenAPI version
    if new_schema.get("openapi") != ready_schema.get("openapi"):
        raise ValueError("OpenAPI versions do not match between schemas.")

    # Merge the "info" section
    merged_info = ready_schema.get("info", {}).copy()
    merged_info.update(new_schema.get("info", {}))

    # Merge the "paths" section
    merged_paths = ready_schema.get("paths", {}).copy()
    for path, methods in new_schema.get("paths", {}).items():
        if path not in merged_paths:
            merged_paths[path] = methods
        else:
            for method, operation in methods.items():
                merged_paths[path][method] = operation

    # Construct the merged schema
    merged_schema = {
        "openapi": ready_schema["openapi"],
        "info": merged_info,
        "paths": merged_paths,
    }

    return merged_schema
