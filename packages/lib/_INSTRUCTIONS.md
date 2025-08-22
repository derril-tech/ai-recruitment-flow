# Lib Package Instructions

## Purpose
This package contains shared utilities, types, and common functionality used across the Recruitment Flow AI application.

## Core Components
1. **Types**: Shared TypeScript interfaces and types
2. **Utilities**: Common helper functions and utilities
3. **Constants**: Application constants and configurations
4. **Validators**: Zod schemas for data validation
5. **API Clients**: Shared API client implementations

## Development Guidelines
- Keep utilities pure and stateless where possible
- Use TypeScript for type safety
- Implement proper error handling
- Include comprehensive JSDoc documentation
- Maintain backward compatibility
- Use Zod for runtime validation

## Library Structure
```
src/
  types/
    common.ts
    api.ts
    models.ts
    enums.ts
  utils/
    date.ts
    string.ts
    validation.ts
    encryption.ts
    formatting.ts
  constants/
    api.ts
    config.ts
    messages.ts
  validators/
    schemas.ts
    validators.ts
  clients/
    api_client.ts
    http_client.ts
  index.ts
```

## TODO: Implement Core Utilities
- [ ] Type definitions (interfaces, enums, types)
- [ ] Date utilities (formatting, parsing, calculations)
- [ ] String utilities (formatting, validation, sanitization)
- [ ] Validation utilities (Zod schemas, custom validators)
- [ ] API client utilities (HTTP client, error handling)
- [ ] Encryption utilities (hashing, encoding, security)

## Utility Categories
- **Types**: Shared interfaces for API responses, models, enums
- **Date**: Date formatting, timezone handling, relative time
- **String**: Text processing, formatting, validation
- **Validation**: Zod schemas, custom validators, type guards
- **API**: HTTP client, error handling, request/response types
- **Security**: Encryption, hashing, token handling

## Testing Requirements
- Unit tests for all utilities
- Type safety testing
- Performance testing for critical functions
- Edge case testing
