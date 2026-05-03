# Backend API Design Playbook

## When to Use

Use this playbook for:

- REST API design
- management/admin API design
- user system APIs
- permission system APIs
- OpenAPI planning
- FastAPI, Express, NestJS, Django, or similar backend API design

Do not use it as the only source for database-only or deployment-only tasks.

## Read First

- [Backend AGENT_USAGE](../AGENT_USAGE.md)
- [Backend Rules Index](../rules/index.md)
- [Backend Topics Index](../wiki/topics/index.md)
- [Backend Patterns Index](../wiki/patterns/index.md)
- [Backend Checklists Index](../wiki/checklists/index.md)
- [Backend Templates Index](../wiki/templates/index.md)
- [Agent Workflow AGENT_USAGE](../../agent_workflow/AGENT_USAGE.md)

## Core Rule Files

- [API Design Rules](../rules/api-design-rules.md)
- [Database Modeling Rules](../rules/database-modeling-rules.md)
- [Auth and Permission Rules](../rules/auth-and-permission-rules.md)
- [Backend Layered Architecture Rules](../rules/backend-layered-architecture-rules.md)
- [Error Handling and Logging Rules](../rules/error-handling-and-logging-rules.md)
- [Backend Security Checklist](../rules/backend-security-checklist.md)

## Useful Patterns and Templates

- [API Response Wrapper Pattern](../wiki/patterns/api-response-wrapper-pattern.md)
- [Error Code System Pattern](../wiki/patterns/error-code-system-pattern.md)
- [JWT Refresh Token Pattern](../wiki/patterns/jwt-refresh-token-pattern.md)
- [RBAC Permission Pattern](../wiki/patterns/rbac-permission-pattern.md)
- [API Response Template](../wiki/templates/api-response-template.md)
- [OpenAPI Doc Template](../wiki/templates/openapi-doc-template.md)

## Task Intake Checklist

- Business objects
- User roles
- Permission boundaries
- Data model assumptions
- API style
- Pagination, filtering, and sorting requirements
- Idempotency, audit, and logging requirements
- OpenAPI or documentation requirement
- Validation and error-handling expectations

## Execution Steps

1. Identify resources and bounded context.
2. Design the endpoint map.
3. Define request and response schemas.
4. Define the unified error envelope.
5. Define auth and permission assumptions.
6. Define pagination, filtering, and sorting rules.
7. Define validation and test cases.
8. Produce the implementation plan.

## Must Include in Output

- Endpoint map
- Request and response schema
- Error format
- Auth and permission assumptions
- Database or model assumptions
- Validation rules
- Test plan
- Remaining uncertainty

## Avoid

- Complex business logic in controllers
- Inconsistent error formats
- Ignoring permission boundaries
- Missing pagination, idempotency, or audit notes
- Reading raw GitHub projects as default guidance
- Introducing queues, Redis, or microservices without task evidence

## Completion Check

- Every endpoint has auth and validation assumptions.
- Response and error formats are consistent.
- Data model assumptions are explicit.
- Tests cover success, validation failure, auth failure, and not-found cases.
- The final answer names the rules, patterns, and templates used.
