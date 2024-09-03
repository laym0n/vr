# Team wr

## Collaborators
Victor Kochnev <br>
Artyom Polienko <br>
Eugenii Solozobov <br>
Nikita Verhovod <br>

## Topic
A typical ingress implementation in k8s forwards incoming traffic to a particular application. An improved API Gateway would integrate Single Sign-On, automatic OpenAPI schema generation, request validation and response caching. The goal of the project is to develop such a Kubernetes operator to extend existing ingress implementations to API Gateway. The project should provide means to define API schema using Custom Resource Definitions in K8s directly and generate them from the source code following a set of conventions.

## Stackholders
* backend developer
* devops
* qa
* software architechure
* project manager
* cyber security team
* api consumers
* end consumers
* business analists

## Features
1. Single Sign-On (SSO): Integrates SSO functionality, allowing for secure and unified access management across all API endpoints. This enhances security by simplifying user authentication and authorization processes.
2. Automatic OpenAPI Schema Generation: Automatically generates OpenAPI schemas from the source code, ensuring that the API documentation is always up-to-date with the actual implementation. This reduces manual effort and minimizes the risk of discrepancies between the documentation and the code.
3. Request Validation: Implements request validation based on the generated API schemas. This ensures that incoming requests conform to the defined structure and data types, improving the robustness and reliability of the system.
4. Response Caching: Includes response caching mechanisms to optimize performance by reducing the load on backend services. Frequently accessed responses are cached, improving response times and reducing latency for end-users.
