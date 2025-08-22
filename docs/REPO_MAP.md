# Repository Map - Recruitment Flow AI

This document provides a comprehensive overview of the project structure and the purpose of each folder and file in the Recruitment Flow AI repository.

## 📁 Root Structure

```
recruitment-flow-ai/
├── apps/                    # Application packages
│   ├── web/                # Next.js 14 frontend application
│   └── api/                # FastAPI backend application
├── packages/               # Shared packages and libraries
│   ├── ui/                 # Shared UI components
│   ├── workflows/          # LangGraph workflow definitions
│   ├── agents/             # CrewAI agent definitions
│   ├── retrievers/         # LangChain retriever tools
│   ├── parsers/            # Document parsing utilities
│   └── lib/                # Shared utilities and types
├── docs/                   # Project documentation
├── infra/                  # Infrastructure and deployment
└── tests/                  # End-to-end tests
```

## 🎯 Apps Directory

### `/apps/web` - Frontend Application (Next.js 14)

**Purpose**: The main frontend application built with Next.js 14, React 18, TypeScript, and Tailwind CSS.

**Key Features**:
- Modern React with App Router
- TypeScript for type safety
- Tailwind CSS for styling
- Dark/light theme support
- Responsive design
- Accessibility (WCAG 2.1 AA)

**Structure**:
```
apps/web/
├── src/
│   ├── app/               # Next.js App Router pages
│   │   ├── dashboard/     # Dashboard pages
│   │   ├── roles/         # Role management pages
│   │   ├── candidates/    # Candidate management pages
│   │   ├── interviews/    # Interview management pages
│   │   ├── offers/        # Offer management pages
│   │   └── compliance/    # Compliance and reporting pages
│   ├── components/        # Reusable React components
│   │   ├── ui/           # Base UI components
│   │   ├── forms/        # Form components
│   │   ├── layouts/      # Layout components
│   │   └── features/     # Feature-specific components
│   ├── hooks/            # Custom React hooks
│   ├── lib/              # Utility functions and configurations
│   ├── types/            # TypeScript type definitions
│   └── styles/           # Global styles and Tailwind config
├── public/               # Static assets
└── package.json          # Frontend dependencies
```

### `/apps/api` - Backend Application (FastAPI)

**Purpose**: The main backend API built with FastAPI, Python 3.11, and async SQLAlchemy.

**Key Features**:
- FastAPI for high-performance API
- Async SQLAlchemy 2.0 for database operations
- PostgreSQL with pgvector for vector search
- Redis for caching and queues
- JWT authentication with RBAC
- WebSocket support for real-time updates

**Structure**:
```
apps/api/
├── recruitment_flow_api/
│   ├── main.py           # FastAPI application entry point
│   ├── core/             # Core application modules
│   │   ├── config.py     # Application configuration
│   │   ├── database.py   # Database connection and models
│   │   ├── redis.py      # Redis connection and utilities
│   │   ├── auth.py       # Authentication and authorization
│   │   └── logging.py    # Logging configuration
│   ├── api/              # API routes and endpoints
│   │   └── v1/           # API version 1
│   │       ├── auth.py   # Authentication endpoints
│   │       ├── roles.py  # Role management endpoints
│   │       ├── candidates.py # Candidate endpoints
│   │       ├── interviews.py # Interview endpoints
│   │       └── offers.py # Offer endpoints
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic services
│   ├── utils/            # Utility functions
│   └── tests/            # Backend tests
└── pyproject.toml        # Python project configuration
```

## 📦 Packages Directory

### `/packages/ui` - Shared UI Components

**Purpose**: Reusable UI components that can be shared between different parts of the application.

**Contents**:
- Button components
- Form components
- Modal components
- Data display components
- Navigation components
- Theme utilities

### `/packages/workflows` - LangGraph Workflows

**Purpose**: LangGraph workflow definitions for the recruitment process orchestration.

**Contents**:
- Intake workflow
- Sourcing workflow
- Screening workflow
- Scheduling workflow
- Interview workflow
- Decision workflow
- Offer workflow

### `/packages/agents` - CrewAI Agents

**Purpose**: CrewAI agent definitions for specialized recruitment tasks.

**Contents**:
- Sourcer agent
- Screener agent
- Scheduler agent
- Interview kit curator agent
- Offer analyst agent

### `/packages/retrievers` - LangChain Retrievers

**Purpose**: LangChain retriever tools for document and data retrieval.

**Contents**:
- Resume retriever
- JD retriever
- Policy retriever
- Competency retriever
- Vector store utilities

### `/packages/parsers` - Document Parsers

**Purpose**: Document parsing utilities for resumes, JDs, and other documents.

**Contents**:
- PDF parser
- DOCX parser
- Text parser
- OCR utilities
- Data extraction utilities

### `/packages/lib` - Shared Libraries

**Purpose**: Shared utilities, types, and configurations.

**Contents**:
- Type definitions
- Utility functions
- Constants
- Configuration helpers
- API clients

## 📚 Documentation

### `/docs` - Project Documentation

**Contents**:
- `PROJECT_BRIEF.md` - Complete project specification
- `REPO_MAP.md` - This file (repository structure guide)
- `API_SPEC.md` - API documentation and specifications
- `CLAUDE.md` - AI collaboration guidelines
- `PROMPT_DECLARATION.md` - Project prompt and requirements

## 🏗️ Infrastructure

### `/infra` - Infrastructure and Deployment

**Purpose**: Infrastructure as Code and deployment configurations.

**Contents**:
- Docker configurations
- Kubernetes manifests
- Terraform configurations
- CI/CD pipelines
- Environment configurations

## 🧪 Testing

### `/tests` - End-to-End Tests

**Purpose**: Comprehensive testing suite for the entire application.

**Contents**:
- Playwright E2E tests
- API integration tests
- Performance tests
- Accessibility tests
- Load tests

## 🔧 Configuration Files

### Root Level Configuration

- `package.json` - Root package configuration with workspaces
- `.gitignore` - Git ignore patterns
- `.env.example` - Environment variables template
- `README.md` - Project overview and setup instructions

### Frontend Configuration

- `apps/web/next.config.js` - Next.js configuration
- `apps/web/tailwind.config.js` - Tailwind CSS configuration
- `apps/web/tsconfig.json` - TypeScript configuration
- `apps/web/.eslintrc.js` - ESLint configuration

### Backend Configuration

- `apps/api/pyproject.toml` - Python project configuration
- `apps/api/alembic.ini` - Database migration configuration
- `apps/api/.env.example` - Backend environment variables

## 🚀 Development Workflow

### Getting Started

1. **Clone the repository**
2. **Install dependencies**: `npm run setup`
3. **Set up environment variables**: Copy `.env.example` files
4. **Start development servers**: `npm run dev`

### Development Commands

- `npm run dev` - Start both frontend and backend in development mode
- `npm run build` - Build both applications for production
- `npm run test` - Run all tests
- `npm run lint` - Run linting on both applications
- `npm run format` - Format code with Prettier

### Architecture Principles

1. **Monorepo Structure**: All related code in one repository
2. **Shared Packages**: Reusable components and utilities
3. **Type Safety**: TypeScript throughout the stack
4. **API-First**: Backend designed for frontend consumption
5. **Scalability**: Microservices-ready architecture
6. **Security**: Authentication, authorization, and data protection
7. **Performance**: Optimized for speed and efficiency
8. **Accessibility**: WCAG 2.1 AA compliance

## 📋 TODO Markers

Throughout the codebase, you'll find TODO markers indicating areas that need implementation:

- `TODO: Implement authentication logic`
- `TODO: Add AI integration`
- `TODO: Implement database models`
- `TODO: Add form validation`
- `TODO: Implement real-time updates`

These markers help identify what needs to be completed during development.

## 🔒 Security Considerations

- Environment variables for sensitive data
- JWT tokens for authentication
- Role-based access control (RBAC)
- Input validation and sanitization
- CORS configuration
- Rate limiting
- Audit logging

## 📊 Performance Targets

- API response time: < 300ms (p95)
- Frontend bundle size: < 500KB
- Database query time: < 100ms
- Cache hit ratio: > 90%
- Uptime: 99.9%

This repository structure provides a solid foundation for building a comprehensive recruitment platform with modern technologies and best practices.
