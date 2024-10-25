# Self-documenting API gateway

## Summary
A typical ingress implementation in k8s forwards incoming traffic to a particular application. An improved API Gateway would integrate Single Sign-On, automatic OpenAPI schema generation, request validation and response caching. The goal of the project is to develop such a Kubernetes operator to extend existing ingress implementations to API Gateway. The project should provide means to define API schema using Custom Resource Definitions in K8s directly and generate them from the source code following a set of conventions.

## Collaborators
Victor Kochnev <br>
Eugenii Solozobov <br>
Nikita Verhovod <br>

## Stackholders
* Backend Developers
* DevOps
* Business-system analists
* QA
* Project Manager
* Cyber security team
* API consumers
* Investors
* Society

## Features
1. Single Sign-On (SSO): Integrates SSO functionality, allowing for secure and unified access management across all API endpoints. This enhances security by simplifying user authentication and authorization processes.
    - Obtaining a token using keyCloack authorization.
    - Checking requests for the presence of a valid token.
3. Request Validation: Implements request validation based on the generated API schemas. This ensures that incoming requests conform to the defined structure and data types, improving the robustness and reliability of the system.
4. Response Caching: Includes response caching mechanisms to optimize performance by reducing the load on backend services. Frequently accessed responses are cached, improving response times and reducing latency for end-users.
5. Automatic OpenAPI Schema Generation Based on File Definition: Automatically generates OpenAPI schemas from the definition of files from K8S services, ensuring that the API documentation is always up-to-date with the actual implementation.
6. Automatic OpenAPI Schema Generation Based on User Request: The user sends a request to the API Gateway, and the system automatically generates and save an OpenAPI schema based on the metadata associated with their request, including parameters and methods.
    - OpenAPI Schema generation based on a user request in case of the successful service response.
    - Updating the OpenAPI Schema of a service. The scheme of a successful request is merged with the scheme of the service
    - Saving valid OpenAPI Schema of a successful request.
      - Saving the scheme of a successful request.
      - Saving up-to-date service scheme.
    - The ability to view saved OpenAPI schemas.
      - View the schema by the ID of the successful request.
      - View the current service scheme.

## Constraints
1. Services behind the gateway must stick to set of convensions for schema definition.
2. The API Gateway must be deployed in a Kubernetes environment, leveraging native K8s resources like Custom Resource Definitions (CRDs), Operators, and Ingress Controllers for managing traffic and API schemas.
3. The gateway must strictly adhere to the OpenAPI standard when generating schemas, ensuring consistency, usability, and widespread compatibility with external tools and services.
4. Any introduced features, including request validation and response caching, should not introduce significant latency, especially for high-throughput applications.
5. All communication between the API Gateway, services, and external clients must occur over industry-standard encryption protocols.
   
## Roles

### Solution Architect
Designs the system’s architecture for scalability and availability. Primarily uses the service for managing API traffic with a focus on high performance.

#### Pain
* performance concerns of the service
* scalability and maintainability of the service

---

### Developer
Integrates the consumer system with the API Gateway. Uses the Gateway to validate requests against predefined API schemas.

#### Pain
* manual API documentation
* need detailed, up-to-date API documentation

---

### System Analyst
Ensures the services meet business and technical requirements. The automatic API generation feature reduces time spent maintaining documentation and ensures consistency.

#### Pain
* need detailed, up-to-date API documentation
* understanding request validations and error handling of the service

----
## Data Glossary

### API Gateway
An entry point for routing and securing interactions between clients and backend services in Kubernetes.

**Attributes:**
- Request Validation
- Response Caching
- Single Sign-On (SSO)
- OpenAPI Schema Generation

---

### OpenAPI Schema
A structure that defines an API, including its endpoints, request/response formats, and data models.

**Attributes:**
- Endpoints
- HTTP Methods (GET, POST, etc.)
- Request Parameters
- Response Structure
- Data Models

---

### Single Sign-On (SSO)
A security feature that allows users to authenticate once and gain access to multiple services without needing to log in again.

**Attributes:**
- Authentication
- Authorization
- Token Management

---

### Custom Resource Definition (CRD)
A way to define custom API objects in Kubernetes, extending Kubernetes API functionalities by allowing custom resources specific to the API Gateway.

**Attributes:**
- Schema
- Definitions
- Validation Rules
- API Versioning

---

### Request Validation
Ensures that incoming requests adhere to the formatted schema and data types in the OpenAPI specification.

**Attributes:**
- Schema Validation
- Data Type Validation
- Error Handling

---

### Response Caching
Stores responses to reduce backend load and improve response times.

**Attributes:**
- Cache Storage
- Expiration Policy
- Cache Invalidation

---

### Operator
A Kubernetes controller that manages the lifecycle of applications and serves as a schema generator.

**Attributes:**
- Application Management
- Event Handling
- Monitoring

---

### API Consumer
Any user, application, or system that interacts with the API Gateway to access backend services.

**Attributes:**
- API Key/Token
- Request Frequency
- Response Time


## StoryMap
![GitHub Image](/storyMap2.png)


## ClassCandidates
![GitHub Image](/ClassCandidates.jpeg)


## ClassDiagramm
![GitHub Image](/ClassDiagram.jpeg)


## DomainModelDiagram
![GitHub Image](/DomainModelDiagram.jpeg)

## UseCase
![GitHub Image](/usecase1.png)
Prioritization of use cases
1. distribute requests across services
2. check api definitions of each service
``MVP``
---
3. establish secure connections
4. cache responses

## InteractionAnalysis
![GitHub Image](/InteractionAnalysis.jpeg)

## Updated class diagram
![GitHub Image](/UpdatedClassDiagram.jpeg)

## Detailed behavior
![GitHub Image](/state1.png)
This state diagram represents the lifecycle of Distributor. 
The process begins in the "Pending requests" state when a started event is received, transitioning from an initial "started" state. The system can be stopped at any time, transitioning to the end state.

When request received, the flow moves into a sub-state called "Processing request," where multiple stages occur sequentially:

1. Pending validation: The request is validated to ensure it meets the necessary criteria.
2. Pending saving schema: If valid, the request's schema is saved for future use.
3. Pending looking for cache: The system checks whether a cached response for the request already exists.
4. A decision is made based on the cache: If a cached response is found, the flow proceeds to "Returning the response." If no cached response exists, the request goes to the "Routing Request" state.
5. Routing Request: The request is processed, and a response is generated.
6. Request Response Caching: The generated response may be cached for future requests.
