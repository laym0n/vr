# Unified API Gateway Microservices

This guide walks you through setting up and deploying the Unified API Gateway microservices on Kubernetes, covering service setup, Docker containerization, Kubernetes deployment, and interaction examples.

## Microservices Overview

- **Cache Service**: Caches responses to reduce latency.
- **Generate Schema Service**: Generates OpenAPI schemas for routes.
- **Request Validator Service**: Validates incoming requests against schemas.
- **Validation Service**: Interacts with the Generate Schema Service to validate requests dynamically.

## Prerequisites

- Docker
- Kubernetes cluster (Minikube or managed Kubernetes)
- `kubectl` configured

## Directory Structure


## Step-by-Step Guide

### 1. Build Docker Images

Navigate to each service directory and build the Docker images:

```bash
docker build -t <service-name>:<version> .

docker build -t cache-service:v1 .
docker build -t generate-schema-service:v1 .
docker build -t request-validator-service:v1 .
docker build -t validation-service:v1 .
```

## 2. Push Docker Images to Container Registry

After building the Docker images, you need to push them to a container registry (like Docker Hub or a private registry).

Use the following command:

```bash
docker push <registry>/<service-name>:<version>

docker push myregistry/cache-service:v1
docker push myregistry/generate-schema-service:v1
docker push myregistry/request-validator-service:v1
docker push myregistry/validation-service:v1

```
## 3. Deploy Microservices on Kubernetes
Apply Kubernetes Deployment and Service Configurations:
In the kubernetes/ folder, apply the deployment and service configurations by running:
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

# Verify Deployment:
Check the status of the deployed pods with the following command:
```bash
kubectl get pods
```

## 4. Example Usage
Once the services are running, you can interact with them through HTTP requests. Below are examples of how to interact with each service.
Route Requests:
```bash 
curl -X POST http://<api-gateway-ip>/route \
  -H "Content-Type: application/json" \
  -d '{"request": "GET /example"}'
```

# Cache a Response:
Store a response in the cache:
```bash 
curl -X POST http://<api-gateway-ip>/cache \
  -H "Content-Type: application/json" \
  -d '{"response": "{\"message\": \"cached response\"}"}'
```
Retrieve a cached response:
```bash 
curl http://<api-gateway-ip>/cache
```

Validate a Request:
Validate a request against a schema:
```bash 
curl -X POST http://<api-gateway-ip>/validate \
  -H "Content-Type: application/json" \
  -d '{"ready_schema": {...}, "request_data": {...}}'
```

Generate and Retrieve OpenAPI Schemas:
Generate a schema:

```bash 
curl -X POST http://<api-gateway-ip>/generate \
  -H "Content-Type: application/json" \
  -d '{"routes": ["/route"]}'
```

Retrieve an existing schema:
```bash
curl http://<api-gateway-ip>/schema?schemaId=<id>
```
