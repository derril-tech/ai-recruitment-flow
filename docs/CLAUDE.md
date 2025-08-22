# CLAUDE.md — Collaboration & Editing Guidelines

This document is Claude’s onboarding guide.  
It defines the **purpose of the project, coding conventions, editing rules, and collaboration workflow**.  
Claude should always respect these boundaries when generating code.

---

## 📌 Project Overview
- **Name:** Recruitment Flow AI  
- **Purpose:** An intelligent hiring orchestration platform that automates role intake, job description creation, sourcing, screening, interview scheduling, evaluation, and offer workflows—while enforcing fairness, compliance, and auditability. Built on Next.js 14 + FastAPI + PostgreSQL/pgvector + Redis, orchestrated by LangGraph with CrewAI agents and LangChain tools.  
- **Target Users:** High growth teams, enterprise TA, RPOs, and internal mobility programs  
- **Goals:** Reduce time to hire by 60-80%, improve candidate experience, ensure compliance and fairness, provide auditable hiring decisions  
- **Tech Stack:**  
  - Frontend: Next.js 14 + React 18 + TypeScript + Tailwind CSS + React Query + Zustand  
  - Backend: FastAPI + Python 3.11 + Async SQLAlchemy 2.0 + PostgreSQL + Redis  
  - Services: OpenAI, Anthropic, LangChain, LangGraph, CrewAI, ChromaDB, ATS integrations, calendar integrations  

---

## 📂 Folder & File Structure
- **apps/web/** → Next.js frontend (React/TS components, pages, hooks, styles)  
- **apps/api/** → FastAPI backend (API, models, services, database, config)  
- **packages/ui/** → Shared UI components  
- **packages/workflows/** → LangGraph workflows  
- **packages/agents/** → CrewAI agents  
- **packages/retrievers/** → LangChain retrievers  
- **packages/parsers/** → Document parsers  
- **packages/lib/** → Shared utilities and types  
- **docs/** → Specs (`REPO_MAP.md`, `API_SPEC.md`, `PROMPT_DECLARATION.md`, `CLAUDE.md`)  
- **scripts/** → Utility scripts (dev runner, seeders)  
- **.github/** → CI/CD workflows  

### Editable by Claude
- `apps/web/src/**/*` (except `_INSTRUCTIONS.md`)  
- `apps/api/recruitment_flow_api/**/*` (except migrations unless asked)  
- `packages/*/src/**/*` (except `_INSTRUCTIONS.md`)  
- Tests in `apps/web/tests/` and `apps/api/tests/`  

### Do Not Touch
- Lockfiles (`package-lock.json`, `poetry.lock`, etc.)  
- CI/CD configs (`.github/workflows/*`) unless explicitly requested  
- Auto-generated code or migrations  
- This file (`CLAUDE.md`)  

---

## 🎨 Coding Conventions
- **Languages:** TypeScript (frontend), Python (backend)  
- **Style Guides:**  
  - Frontend: Prettier + ESLint (Next.js core-web-vitals + TypeScript recommended)  
  - Backend: Black + ruff + mypy (PEP8 + type checking)  
- **Naming:**  
  - Components: `PascalCase`  
  - Variables: `camelCase` (TS), `snake_case` (Python)  
  - Files: `kebab-case` for components, `snake_case` for utilities  
  - Branches: `feature/…`, `fix/…`, `hotfix/…`  
- **Commenting:**  
  - Document public components, functions, and non-obvious logic  
  - Use `// TODO:` or `# TODO:` for clear tasks  
  - Include JSDoc for complex functions and components  
  - Add inline comments for business logic and edge cases  

---

## 🤝 AI Collaboration Rules
- Always respond with **full file rewrites** if >30 lines are changed.  
- Keep responses **concise in explanation, complete in code**.  
- Never remove error handling, logging, or comments unless replacing them with better versions.  
- Preserve imports and typing.  
- If ambiguity arises:  
  1. Ask up to **2 clarifying questions**  
  2. If unanswered, proceed with best guess and note assumptions  

---

## ✍️ Editing Rules
- **Editable Files:** All app source code under `frontend/src/` and `backend/app/`  
- **Avoid:** lockfiles, auto-generated files, CI configs  
- **Format of Responses:**  
  - Full file rewrites for large changes  
  - Patches (with clear diff context) for small fixes  
- **Error Handling:** must remain in place at all times  

---

## 📦 Project Dependencies
- **Frontend:** Next.js 14, React 18, TypeScript, Tailwind CSS, React Query, Zustand, Headless UI, Heroicons, Radix UI, clsx, class-variance-authority, lucide-react, react-hook-form, zod, date-fns, react-hot-toast, socket.io-client, axios, framer-motion, recharts  
- **Backend:** FastAPI, Python 3.11, Async SQLAlchemy 2.0, PostgreSQL, Redis, JWT, Pydantic, Uvicorn, python-multipart, python-jose, passlib, python-dotenv, alembic, psycopg2-binary, asyncpg, openai, anthropic, langchain, langgraph, crewai, chromadb, sentence-transformers, pandas, numpy, pydantic, pydantic-settings, python-magic, PyPDF2, python-docx, openpyxl, pillow, aiosmtplib, jinja2, google-auth, msal, pytest, httpx, black, isort, ruff, mypy, pre-commit  
- **Services:** OpenAI GPT-4, Anthropic Claude, LangChain, LangGraph, CrewAI, ChromaDB, PostgreSQL with pgvector, Redis, ATS integrations (Greenhouse, Lever, Workday), Calendar integrations (Google, Microsoft), Email services (SMTP), File storage (AWS S3)  
- **Environment:**  
  - Variables in `env.example` must be respected  
  - Secrets should never be hardcoded  
  - Use environment-specific configurations for development/production  

---

## 🛠️ Workflow & Tools
- **Run locally:**  
  - Full stack: `./scripts/dev.sh` (starts both frontend and backend)  
  - Frontend only: `cd apps/web && npm run dev`  
  - Backend only: `cd apps/api && uvicorn recruitment_flow_api.main:app --reload`  
- **FE ↔ BE boundary:** REST JSON via `/api/v1/*`, WebSockets for real-time updates  
- **Testing:**  
  - Frontend: Jest + React Testing Library  
  - Backend: Pytest + httpx  
  - E2E: Playwright  
- **CI/CD:** GitHub Actions (lint, type-check, test, build, security scan)  
- **Deployment:** Vercel (frontend) + Render (backend)  
- **Code Quality:** Pre-commit hooks, conventional commits, automated formatting  

---

## 📚 Contextual Knowledge
- **Design System:** Tailwind CSS with custom color palettes (primary, secondary, success, warning, error), Inter font family, custom spacing and animations, dark/light theme support  
- **Domain Rules:** 
  - All AI outputs must provide citations and rationale
  - Fairness checks must pass for all hiring decisions
  - Human approval gates required for outreach and decisions
  - Audit trails must be maintained for all actions
  - GDPR/CCPA compliance for candidate data
  - EEO/DEI reporting requirements
- **Scaffolding Rules:** 
  - Monorepo structure with npm workspaces
  - Shared packages for UI, workflows, agents, retrievers, parsers, lib
  - Consistent API patterns across all endpoints
  - Type safety throughout the application
- **UX Principles:** 
  - WCAG 2.1 AA accessibility compliance
  - Empty/loading/error states for all async operations
  - Responsive design for all screen sizes
  - Keyboard-first navigation
  - Reduced motion support
  - Real-time updates via WebSockets  

---

## ✅ Examples

**Good Answer Example**
```tsx
// Good: Full file rewrite, assumptions stated, comments kept
import { useEffect, useState } from "react";
import { fetchCandidates } from "@/lib/api";
import { Candidate } from "@/types/candidate";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { LoadingSpinner } from "@/components/ui/loading-spinner";

// CLAUDE_TASK: Fetch and display candidate list with loading/error states
export default function CandidateList() {
  const [candidates, setCandidates] = useState<Candidate[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchCandidates()
      .then(setCandidates)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;
  if (error) return <div className="text-red-500">Error: {error}</div>;
  
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {candidates.map(candidate => (
        <Card key={candidate.id}>
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              {candidate.name}
              <Badge variant={candidate.status === 'active' ? 'success' : 'secondary'}>
                {candidate.status}
              </Badge>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-gray-600">{candidate.email}</p>
            <p className="text-sm text-gray-600">{candidate.role}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
```

**Bad Answer Example**
```tsx
// Bad: Incomplete, no error handling, no types, no accessibility
export default function CandidateList() {
  const [candidates, setCandidates] = useState([]);

  useEffect(() => {
    fetch('/api/candidates').then(r => r.json()).then(setCandidates);
  }, []);

  return (
    <div>
      {candidates.map(c => <div>{c.name}</div>)}
    </div>
  );
}
```

---

## 🎯 Performance & Quality Standards
- **Performance Targets:**
  - API response time: p95 < 300ms
  - Chat streaming TTFB: < 500ms
  - Scheduler responses: < 2s
  - Frontend bundle size: < 500KB (gzipped)
  - Lighthouse score: ≥ 95
- **Quality Standards:**
  - Test coverage: > 90%
  - TypeScript strict mode enabled
  - All linting rules must pass
  - No console.log in production code
  - Proper error boundaries and fallbacks
- **Security Requirements:**
  - JWT token validation on all protected routes
  - Input sanitization and validation
  - Rate limiting on all endpoints
  - CORS properly configured
  - No sensitive data in client-side code

---

## 🔄 Development Workflow
1. **Feature Development:**
   - Create feature branch from `develop`
   - Implement feature with tests
   - Update documentation if needed
   - Create pull request
2. **Code Review:**
   - All code must be reviewed
   - Tests must pass
   - Linting and formatting must pass
   - Performance impact assessed
3. **Deployment:**
   - Automated deployment on merge to `main`
   - Staging environment for testing
   - Production deployment with rollback capability

---

## 📋 Checklist for Claude
Before submitting any code changes, ensure:
- [ ] All TypeScript types are properly defined
- [ ] Error handling is implemented
- [ ] Loading states are included
- [ ] Accessibility features are added
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] Performance impact is considered
- [ ] Security best practices are followed




