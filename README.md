# Recruitment Flow AI

**Intelligent Hiring Orchestration Platform**

> Source. Screen. Schedule. Decide—fairly and fast.

Recruitment Flow AI is an end-to-end hiring orchestration platform that automates role intake, job description creation, sourcing, screening, interview scheduling, evaluation, and offer workflows—while enforcing fairness, compliance, and auditability.

## 🚀 Features

### Core Capabilities
- **Role Intake & JD Studio**: Capture success profiles, competencies, and generate bias-checked job descriptions
- **Sourcing Hub**: Ingest resumes, LinkedIn profiles, and ATS exports with deduplication
- **AI-Powered Screening**: RAG-grounded candidate evaluation with competency mapping
- **Smart Scheduling**: Timezone-aware interview scheduling with calendar integrations
- **Interview Orchestration**: Structured rubrics, bias interruption, and real-time scoring
- **Decision Support**: Score aggregation, calibration, and auditable rationales
- **Compliance & Reporting**: EEO/OFCCP reporting, GDPR compliance, and audit trails

### AI Integration
- **LangGraph Workflows**: Deterministic recruitment pipelines
- **CrewAI Agents**: Specialized agents for sourcing, screening, and scheduling
- **LangChain Tools**: Document parsing and vector retrieval
- **RAG System**: Grounded evaluations using candidate materials and role competencies

## 🏗️ Architecture

### Tech Stack
- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11, Async SQLAlchemy 2.0
- **Database**: PostgreSQL with pgvector for vector search
- **Cache**: Redis for caching and queues
- **AI**: OpenAI GPT-4, Anthropic Claude, LangGraph, CrewAI
- **Deployment**: Vercel (frontend), Render (backend)

### Project Structure
```
recruitment-flow-ai/
├── apps/
│   ├── web/                 # Next.js frontend
│   └── api/                 # FastAPI backend
├── packages/
│   ├── ui/                  # Shared UI components
│   ├── workflows/           # LangGraph workflows
│   ├── agents/              # CrewAI agents
│   ├── retrievers/          # LangChain tools
│   ├── parsers/             # Document parsing
│   └── lib/                 # Shared utilities
├── docs/                    # Documentation
├── infra/                   # Infrastructure
└── tests/                   # End-to-end tests
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- PostgreSQL 14+
- Redis 6+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/recruitment-flow-ai.git
   cd recruitment-flow-ai
   ```

2. **Install dependencies**
   ```bash
   npm run setup
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

4. **Set up the database**
   ```bash
   # Create PostgreSQL database
   createdb recruitment_flow_dev
   
   # Run migrations
   cd apps/api
   alembic upgrade head
   ```

5. **Start development servers**
   ```bash
   npm run dev
   ```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📚 Documentation

- [Project Brief](./docs/PROJECT_BRIEF.md) - Complete project specification
- [Repository Map](./docs/REPO_MAP.md) - Project structure guide
- [API Specification](./docs/API_SPEC.md) - API documentation
- [Claude Guidelines](./docs/CLAUDE.md) - AI collaboration guidelines

## 🔧 Development

### Available Scripts

```bash
# Development
npm run dev              # Start both frontend and backend
npm run dev:frontend     # Start frontend only
npm run dev:backend      # Start backend only

# Building
npm run build            # Build both applications
npm run build:frontend   # Build frontend
npm run build:backend    # Build backend

# Testing
npm run test             # Run all tests
npm run test:frontend    # Run frontend tests
npm run test:backend     # Run backend tests
npm run test:e2e         # Run end-to-end tests

# Linting and Formatting
npm run lint             # Lint both applications
npm run format           # Format code with Prettier
```

### Code Quality

- **TypeScript**: Strict type checking throughout
- **ESLint**: Code linting with Next.js and TypeScript rules
- **Prettier**: Code formatting
- **Black**: Python code formatting
- **Ruff**: Python linting
- **MyPy**: Python type checking

## 🔒 Security & Compliance

### Security Features
- JWT authentication with refresh tokens
- Role-based access control (RBAC)
- Input validation and sanitization
- Rate limiting and DDoS protection
- Audit logging for all actions

### Compliance Features
- GDPR/CCPA compliance with data retention policies
- EEO/OFCCP reporting capabilities
- Adverse impact monitoring
- Candidate data portability and deletion
- Immutable audit trails

## 📊 Performance Targets

- **API Response Time**: < 300ms (p95)
- **Frontend Bundle Size**: < 500KB
- **Database Query Time**: < 100ms
- **Cache Hit Ratio**: > 90%
- **Uptime**: 99.9%

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow the existing code style and conventions
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [docs.recruitment-flow.ai](https://docs.recruitment-flow.ai)
- **Issues**: [GitHub Issues](https://github.com/your-org/recruitment-flow-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/recruitment-flow-ai/discussions)

## 🙏 Acknowledgments

- Built with [Next.js](https://nextjs.org/)
- Powered by [FastAPI](https://fastapi.tiangolo.com/)
- AI capabilities by [OpenAI](https://openai.com/) and [Anthropic](https://www.anthropic.com/)
- Workflow orchestration by [LangGraph](https://github.com/langchain-ai/langgraph)
- Agent framework by [CrewAI](https://github.com/joaomdmoura/crewAI)

---

**Recruitment Flow AI** - Making hiring faster, fairer, and more efficient.