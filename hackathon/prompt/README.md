# Microservices Development Workflow: Request-Response Log

## История запросов и ответов

[Посмотреть историю запросов и ответов](https://chatgpt.com/share/674ecc40-ccd8-800f-a97f-16c4a7a4935d)

### 1. Микросервис OpenAPI Schema Generator

**Запрос:**
> A typical ingress implementation in k8s forwards incoming traffic to a particular application. An improved API Gateway would integrate Single Sign-On, automatic OpenAPI schema generation, request validation and response caching. The goal of the project is to develop such a Kubernetes operator to extend existing ingress implementations to API Gateway. The project should provide means to define API schema using Custom Resource Definitions in K8s directly and generate them from the source code following a set of conventions.
> Write on Python microservice that can accept requests from other microservices via http. The main purpose that microservice is to generate openApi schema from HTTP request. HTTP request not contains info about OpenApi schema. Microservice must parse request and make a schema based on the request

**Ответ:**
```
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

app = FastAPI(title="OpenAPI Schema Generator")

class SchemaResponse(BaseModel):
    openapi: str
    info: Dict[str, Any]
    paths: Dict[str, Any]

@app.post("/generate-schema", response_model=SchemaResponse)
async def generate_schema(request: Request):
    """
    Generate OpenAPI schema based on the incoming HTTP request.
    """
    # Extract method and path from the request
    method = request.method.lower()
    url_path = str(request.url.path)
    
    # Extract headers
    headers = {key: value for key, value in request.headers.items()}

    # Extract query parameters
    query_params = {key: value for key, value in request.query_params.items()}

    # Extract body (if any)
    body = await request.json() if "application/json" in headers.get("content-type", "") else {}

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
```

### 2. Добавление метода `generate_schema`

**Запрос:**
> Great work! Can you add method generate schema that accepts request and response?

**Ответ:**
```
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any, Optional

app = FastAPI(title="OpenAPI Schema Generator")

class SchemaResponse(BaseModel):
    openapi: str
    info: Dict[str, Any]
    paths: Dict[str, Any]

def generate_schema(request: Request, response_body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Generate OpenAPI schema based on the incoming HTTP request and expected response.
    :param request: The HTTP request object.
    :param response_body: Optional response body structure as a dictionary.
    :return: OpenAPI schema as a dictionary.
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
        body = request.state.body if hasattr(request.state, "body") else {}

    # Construct schema for the response
    response_schema = {
        "200": {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {key: {"type": "string"} for key in response_body.keys()} if response_body else {}
                    }
                }
            },
        }
    } if response_body else {}

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
                    "description": "This endpoint was dynamically generated based on the request and expected response.",
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
                    "responses": response_schema,
                }
            }
        },
    }
    return schema

@app.post("/generate-schema", response_model=SchemaResponse)
async def generate_schema_endpoint(request: Request, response_body: Optional[Dict[str, Any]] = None):
    """
    Generate OpenAPI schema based on the incoming HTTP request and optional expected response.
    """
    # To handle request body, store it in request.state
    if "application/json" in request.headers.get("content-type", ""):
        request.state.body = await request.json()

    schema = generate_schema(request, response_body)
    return schema

```

---

### 3. Объединение схем

**Запрос:**
> Great work! But can you add to parameters ready OpenApi Schema and remove response parameter? That microservice must generate OpenApi Schema from request and merge that Schema with ready OpenApi Schema and return result Schema
**Ответ:**
```
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="OpenAPI Schema Generator")

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

```

---

### 4. Микросервис "Request Validator"

**Запрос:**
> Great work! I need you to write microservice "Request Validator" on Python. That microservice must accept request via HTTP, send ready to use OpenApi schema and request to microservice Generate-Schema, accept response from microservice Generate-Schema, save result schema and validate request on result Schema

**Ответ:**
```
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import httpx
from jsonschema import validate, ValidationError

app = FastAPI(title="Request Validator")

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

```

---

### 5. Микросервис "Cache"

**Запрос:**
> Great work! Now i need you to write microservice "Response cacher" on Python. That microservice must accept requests via http. Microservice must contain 2 endpoints. One for save response with idempotentKey and the second for get response with idempotentKey

**Ответ:**
```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Response Cacher")

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

```

---

### 6. Микросервис "Distributor"

**Запрос:**
> Great work! Now i need you to write microservice "Request distributor". That microservice accepts request, send that request to microservice "Request Validator", then if request is valid, tries to find cached response in microservice Cache, if cache exists return cached response else distribute request to original service (API Gateway) and save response in Cache service

**Ответ:**
```
from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
import httpx
from typing import Dict, Any

app = FastAPI(title="Request Distributor")

# Microservice URLs
VALIDATOR_URL = "http://request-validator-service:8001/validate-request"
CACHE_URL = "http://response-cacher-service:8002"
API_GATEWAY_URL = "http://api-gateway-service:8003"

# Request models
class RequestDistributor(BaseModel):
    idempotentKey: str
    readySchema: Dict[str, Any]
    requestData: Dict[str, Any]

@app.post("/distribute-request")
async def distribute_request(request: RequestDistributor):
    """
    Accepts a request, validates it, checks for a cached response, or forwards it to the API Gateway.
    """
    # Step 1: Validate the request with Request Validator
    validation_payload = {
        "ready_schema": request.readySchema,
        "request_data": request.requestData
    }

    try:
        async with httpx.AsyncClient() as client:
            validation_response = await client.post(
                f"{VALIDATOR_URL}", json=validation_payload
            )
            validation_response.raise_for_status()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Request Validator: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=400, detail=f"Validation failed: {e.response.json()}")

    # Step 2: Check if the response is cached
    try:
        async with httpx.AsyncClient() as client:
            cache_response = await client.get(
                f"{CACHE_URL}/get-response", params={"idempotentKey": request.idempotentKey}
            )
            if cache_response.status_code == 200:
                cached_response = cache_response.json()
                return {"source": "cache", "response": cached_response["response"]}
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting Response Cacher: {e}")
    except httpx.HTTPStatusError:
        # Cache miss, continue to original service
        pass

    # Step 3: Forward the request to the original service (API Gateway)
    try:
        async with httpx.AsyncClient() as client:
            original_service_response = await client.post(
                f"{API_GATEWAY_URL}", json=request.requestData
            )
            original_service_response.raise_for_status()
            original_response_data = original_service_response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error contacting API Gateway: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"API Gateway returned an error: {e.response.json()}")

    # Step 4: Save the response in the cache
    cache_payload = {
        "idempotentKey": request.idempotentKey,
        "response": original_response_data
    }
    try:
        async with httpx.AsyncClient() as client:
            cache_save_response = await client.post(
                f"{CACHE_URL}/cache-response", json=cache_payload
            )
            cache_save_response.raise_for_status()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error saving response in cache: {e}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"Cache service returned an error: {e.response.json()}")

    # Step 5: Return the original service response
    return {"source": "api-gateway", "response": original_response_data}

```
