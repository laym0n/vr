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

docker buildx build --platform linux/amd64 -t verhovnick/cache-service:v11 --push .
docker buildx build --platform linux/amd64 -t verhovnick/generate-schema-service:v7 --push .
docker buildx build --platform linux/amd64 -t verhovnick/request-validator-service:v7 --push .
docker buildx build --platform linux/amd64 -t verhovnick/validation-service:v8 --push .
docker buildx build --platform linux/amd64 -t verhovnick/authentication-service:v3 --push .
docker buildx build --platform linux/amd64 -t verhovnick/storage-service:v4 --push .

```

## 2. Push Docker Images to Container Registry

After building the Docker images, you need to push them to a container registry (like Docker Hub or a private registry).

Use the following command:

```bash
docker push <registry>/<service-name>:<version>

docker push verhovnick/cache-service:v3
docker push verhovnick/generate-schema-service:v3
docker push verhovnick/request-validator-service:v4
docker push verhovnick/validation-service:v4

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
# Prompts to GPT
## 1. Goal Identification
```bash
Identify microservices frameworks optimized for Kubernetes-based API Gateways, emphasizing features like OpenAPI support, SSO, and caching.
```

## 1. Goal Identification
```bash
Identify microservices frameworks optimized for Kubernetes-based API Gateways, 
emphasizing features like OpenAPI support, SSO, and caching.
```
## Prompt response
![GitHub Image](/hackathon/pics/prompt_1.png)

## 2. Evaluation Matrix
```bash
Compare Spring Cloud Gateway, Envoy Proxy. 
Evaluate them for performance, scalability, and community support, scoring each from 1 to 5. 
Justify each score briefly.
```
## Prompt response
![GitHub Image](/hackathon/pics/prompt_2.png)

## 3. Shortlisting
```bash
Based on the evaluation scores, 
select the top two frameworks that best align with Kubernetes-based 
API Gateway requirements and support OpenAPI handling, SSO, and caching. 
Explain why these two were chosen.
```

## Prompt response
![GitHub Image](/hackathon/pics/prompt_3.png)


## 4. Detailed Comparison
```bash
Perform a detailed comparison of Spring Cloud Gateway and Envoy Proxy 
for OpenAPI handling, caching mechanisms, and SSO support. 
Assess Kubernetes integration and scalability in 
distributed environments.
```
## Prompt response
![GitHub Image](/hackathon/pics/prompt_4.png)

## 5. Final Selection
```bash
Choose the better framework for Kubernetes-based 
API Gateway considering OpenAPI handling, caching efficiency, and SSO support. 
Provide a clear justification and link to resources for implementation.
```

## Prompt response
![GitHub Image](/hackathon/pics/prompt_5.png)

## 6. Choose framework
```bash
Generate a 'Hello World' microservice using Envoy Proxy that exposes 
a POST /generate endpoint to create OpenAPI schemas 
for a list of routes. Use REDIS for caching and secure communication via OIDC.
```
## Prompt response 6.1
![GitHub Image](/hackathon/pics/prompt_6_1.png)
## Prompt response 6.2
![GitHub Image](/hackathon/pics/prompt_6_2.png)
## Prompt response 6.3
![GitHub Image](/hackathon/pics/prompt_6_3.png)
