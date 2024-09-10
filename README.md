# Self-documenting API gateway

## Summary
A typical ingress implementation in k8s forwards incoming traffic to a particular application. An improved API Gateway would integrate Single Sign-On, automatic OpenAPI schema generation, request validation and response caching. The goal of the project is to develop such a Kubernetes operator to extend existing ingress implementations to API Gateway. The project should provide means to define API schema using Custom Resource Definitions in K8s directly and generate them from the source code following a set of conventions.

## Collaborators
Victor Kochnev <br>
Artyom Polienko <br>
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
2. Automatic OpenAPI Schema Generation: Automatically generates OpenAPI schemas from the definition of files from K8S services, ensuring that the API documentation is always up-to-date with the actual implementation.
3. Request Validation: Implements request validation based on the generated API schemas. This ensures that incoming requests conform to the defined structure and data types, improving the robustness and reliability of the system.
4. Response Caching: Includes response caching mechanisms to optimize performance by reducing the load on backend services. Frequently accessed responses are cached, improving response times and reducing latency for end-users.

## Constraints
1. Services behind the gateway must stick to set of convensions for schema definition.
2. The API Gateway must be deployed in a Kubernetes environment, leveraging native K8s resources like Custom Resource Definitions (CRDs), Operators, and Ingress Controllers for managing traffic and API schemas.
3. The gateway must strictly adhere to the OpenAPI standard when generating schemas, ensuring consistency, usability, and widespread compatibility with external tools and services.
4. Any introduced features, including request validation and response caching, should not introduce significant latency, especially for high-throughput applications.
5. All communication between the API Gateway, services, and external clients must occur over industry-standard encryption protocols.
