# THE PROJECT BRIEF #

# Project Name #
recruitment-flow-ai


# Product Description / Presentation #


recruitment-flow-ai
Recruitment Flow AI — Intelligent Hiring Orchestration
Tagline: Source. Screen. Schedule. Decide—fairly and fast.
Important: This system provides hiring decision support, not final decisions. Human review and compliance checks are required at all stages.
________________________________________
1) Product Description / Presentation
Executive Summary
Recruitment Flow AI is an end to end hiring orchestration platform that automates role intake, job description creation, sourcing, screening, interview scheduling, evaluation, and offer workflows—while enforcing fairness, compliance, and auditability. Built on Next.js 14 + FastAPI + PostgreSQL/pgvector + Redis, orchestrated by LangGraph with CrewAI agents and LangChain tools, it blends RAG grounded candidate evaluation, competency based scoring, and deterministic pipelines to reduce time to hire and improve candidate experience without bias.
Business Outcomes
•	Time to screen ↓ 60–80% with automated parsing and competency mapping.
•	Scheduling friction ↓ 70% via multi calendar, time zone aware orchestration.
•	Candidate NPS ↑; structured interviews yield stronger signal and lower variance.
•	Compliance readiness with auditable rationales and EEO/DEI reporting.
________________________________________
Core Capabilities
•	Role Intake & JD Studio: Capture success profile, competencies, level/ladder; generate bias checked JDs with inclusive language recommendations.
•	Sourcing Hub: Ingest resumes/LinkedIn profiles/ATS exports; dedupe; talent pools & silver medalists; outreach sequencing (approval gated).
•	Parsing & Competency Mapping: CV/portfolio parsing; map skills to O*NET/ESCO style ontologies; weight recency/proficiency; gap analysis vs. role.
•	Screening & Shortlists: RAG grounded Q&A over resume + portfolio + code repos; structured screen scores (must/should/could); risk flags with evidence.
•	Scheduling Orchestrator: Time zone aware interviewer finder, load balancing, panel templates; calendar integrations (Google/M365); candidate self serve rescheduling.
•	Interview Kit & Rubrics: Role aligned question banks; anchored rubrics; live score capture; bias interruption cues; panel debrief notes.
•	Decision & Offer: Score aggregation, calibration, rationales; comp bands guidance; offer letter generator; e sign; background check handoff (partner API).
•	Compliance & Reporting: EEO/OFCCP reporting, GDPR/CCPA consent & retention, audit trails, adverse impact monitoring.
•	Candidate 360: Timeline of interactions, documents, feedback, and outcomes; privacy controls and candidate data requests.
________________________________________
Functional Modules (User Journeys)
1.	Intake → role goals, competencies, level, must haves; JD draft with inclusive rewrite.
2.	Source → import pools; enrich (optional); dedupe; outreach sequences.
3.	Screen → automated screen with evidence; human review; shortlist.
4.	Schedule → panel builder, interviewer finder, candidate self serve.
5.	Interview → structured rubrics, notes, anti bias nudges; debrief.
6.	Decide → calibrated decision; rationale & audit; approvals.
7.	Offer → comp guidance, letter generation, e sign; preboarding handoff.
________________________________________
Non Functional Requirements
•	Performance: p95 API < 300ms (cache hit); chat streaming TTFB < 500ms; scheduler responses in < 2s.
•	Scale: 10k+ concurrent users; millions of profiles.
•	Reliability: 99.9% uptime; graceful degradation (manual scheduling, read only search) during provider outages.
•	Security & Privacy: SOC2/ISO27001; encryption at rest/in transit; RLS tenant isolation; consent ledger; data minimization; retention & deletion workflows.
•	Accessibility: WCAG 2.1 AA; keyboard first; reduced motion.
________________________________________
Frontend (Next.js 14 + React 18 + TypeScript + Tailwind)
•	Key Screens
o	Pipeline Board: stage funnels, SLAs, alerts; drag and drop stage moves with audit.
o	JD Studio: inclusive language checker, tone/style controls, brand templates.
o	Talent Pool: advanced filters, boolean + semantic search, similarity groups.
o	Screening Console: side by side resume + evidence; competencies heatmap; risk flags.
o	Scheduler: availability matrix, interviewer load view, candidate reschedule portal.
o	Interview Room: question kit, timers, rubric capture, bias nudges, structured notes.
o	Decision & Offer: score aggregation, rationale composer, approvals, offer builder.
o	Compliance Hub: EEO/DEI dashboards, adverse impact checks, retention policies.
•	UX: WebSockets for live updates; optimistic transitions; dark/light theme; inline toasts for actions.
•	State: React Query (server cache); Zustand/Context (UI state); form hooks; autosave.
________________________________________
Backend (FastAPI + Python 3.11 + Async SQLAlchemy 2.0)
•	Auth: JWT (access/refresh), SSO (SAML/OIDC), MFA; RBAC (admin/recruiter/hiring manager/interviewer/analyst) with row level security.
•	Services: roles, candidates, profiles, pools, parsing, screening, scheduling, interviews, offers, compliance, notifications, audits.
•	Integrations (adapters): ATS (Greenhouse/Lever/Workday Recruiting), calendars (Google/M365), email (SES/Graph), storage (S3/GCS/Drive), video (WebRTC/Zoom), background checks (partners), HRIS handoff.
•	Observability: OpenTelemetry traces, Prometheus metrics, structured logs, cost ledger.
________________________________________
AI Orchestration & Retrieval
•	Framework Choice: LangGraph for deterministic flows (intake → source → screen → schedule → interview → decide → offer) with retries/timeouts; CrewAI agents for role specialized tasks (Sourcer, Screener, Scheduler, Interview Kit Curator, Offer Analyst); LangChain for tools/retrievers; RAG over JDs, competencies, rubrics, policies, and candidate docs.
•	Models: GPT 4 family (synthesis, scoring rationales), Claude (long context reasoning, safety review).
•	Guardrails: cite or refuse; fairness constraints (block use of protected attributes); anonymization options in early stages; uncertainty bands; human approval gates for outreach and decisions.
________________________________________
Data Model (selected)
•	organizations, users(roles, scopes)
•	roles(id, title, level, competencies_json, jd_text, policy_refs)
•	candidates(id, contact_json, consent_flags, source, status)
•	profiles(candidate_id, resume_url, vector, skills_json, experience_json)
•	screens(candidate_id, role_id, evidence_json, scores_json, risk_flags)
•	interviews(role_id, candidate_id, panel_json, slots, outcome, notes_json)
•	schedules(interview_id, availability_json, calendar_events_json)
•	offers(candidate_id, role_id, terms_json, approvals, status)
•	audits(actor, action, resource, purpose, timestamp)
•	reports(type, payload, generated_at)
________________________________________
API Surface (sample)
REST
•	POST /roles → create role & JD; POST /roles/{id}/jd/rewrite (inclusive)
•	POST /candidates/import → bulk ingest; GET /candidates/search
•	POST /screen/{role_id}/{candidate_id} → evidence + scores
•	POST /schedule/{interview_id} → propose slots; POST /schedule/{id}/confirm
•	POST /interview/{id}/submit → rubric scores + notes
•	POST /decide/{role_id} → aggregate & rationale; POST /offer/{candidate_id} → draft
•	GET /compliance/eeo, GET /compliance/adverse_impact
WebSockets
•	/ws/pipeline/{role_id} streaming status, scheduler updates, chat tokens
________________________________________
Security, Privacy & Compliance
•	Fairness & DEI: Remove protected attribute signals; report selection rates; run four fifths rule checks; calibrate thresholds.
•	Privacy: GDPR/CCPA consent tracking; data minimization; candidate deletion/DSAR; region based retention.
•	Auditability: immutable audit logs; rationale capture; versioned JD/playbooks.
•	Secret Hygiene: env only, rotation, least privilege; per integration scopes.
________________________________________
Deployment & Scaling
•	Frontend: Vercel (ISR, edge cache).
•	Backend: Render autoscaling; workers for parsing/embedding/scheduling; Redis queues & rate limits.
•	DB: Postgres + pgvector; PITR; nightly backups.
Env Vars (excerpt)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
DATABASE_URL=
REDIS_URL=
JWT_SECRET=
SMTP_URL=
STORAGE_BUCKET=
GOOGLE_WORKSPACE_CONFIG=
M365_GRAPH_CONFIG=
ATS_CLIENT_ID=/ATS_CLIENT_SECRET=
ALLOWED_ORIGINS=
________________________________________
Success Metrics
•	Time to first screen < 24h for new roles.
•	Interview scheduling success on first pass >85%; no show rate ↓ >20%.
•	Adverse impact deltas within policy thresholds with continuous monitoring.
•	Lighthouse ≥ 95; uptime 99.9%; test coverage >90%.
________________________________________
2) Framework Choice (Why LangGraph + CrewAI + LangChain + RAG)
•	LangGraph provides deterministic, auditable pipelines ideal for regulated HR flows (retries/timeouts/state recovery).
•	CrewAI fits role based collaboration (Sourcer/Screener/Scheduler/Offer Analyst) with human approval steps.
•	LangChain supplies proven retrievers/parsers (resume/JD loaders, vector stores).
•	RAG grounds evaluations in candidate materials + role competencies + policy playbooks for low hallucination and explainability.
________________________________________
3) Dev Team Brief
Goals
Deliver a production ready recruitment platform that automates sourcing→offer while enforcing fairness, privacy, and auditability.
Deliverables
1.	Next.js frontend (Pipeline Board, JD Studio, Talent Pool, Screening Console, Scheduler, Interview Room, Decision & Offer, Compliance Hub).
2.	FastAPI backend (auth, roles/candidates/screens/interviews/offers/compliance) with WebSockets.
3.	Postgres schema with pgvector; Redis queues; search (hybrid vector + keyword).
4.	LangGraph workflows + CrewAI agents; LangChain retrievers; RAG + guardrails.
5.	Integrations: ATS, calendars, email, storage, video, background checks, HRIS handoff.
6.	CI/CD, tests (unit/integration/e2e), OpenAPI docs; Vercel + Render configs.
Milestones
•	M1 (Weeks 1–2): Repos, auth/roles, JD Studio + inclusive checker, candidate import, talent search.
•	M2 (Weeks 3–4): Parsing + competency mapping, screening console, scheduler MVP.
•	M3 (Weeks 5–6): Interview kits + rubrics, decision aggregation, offer builder + e sign.
•	M4 (Weeks 7–8): Compliance hub, adverse impact monitoring, load tests, GA.
Definition of Done
•	All AI outputs provide citations & rationale; fairness checks pass; approvals logged.
•	WCAG 2.1 AA + Lighthouse ≥ 95; tests >90%; OpenAPI published.
•	Data retention/DSAR flows validated; audit trails immutable.
Coding Standards
•	Ruff/Black/mypy; eslint/prettier; pre commit hooks; conventional commits; feature flags.
Repo Structure
/apps
  /web (Next.js 14)
  /api (FastAPI)
/packages
  /ui (tailwind components)
  /workflows (LangGraph graphs)
  /agents (CrewAI roles)
  /retrievers (LangChain tools)
  /parsers (resume/pdf/ocr)
  /lib (shared clients/types)
/infra (IaC, deploy configs)
/tests (backend, frontend, e2e)
________________________________________
Critical Prompts for Claude (Recruitment)
Prompt 1 — Project Setup & Architecture
"Create the complete project structure and architecture for Recruitment Flow AI. Set up Next.js 14 + TypeScript + Tailwind, FastAPI with async SQLAlchemy + JWT/SSO/MFA, PostgreSQL with pgvector, Redis, deploy configs for Vercel (frontend) and Render (backend), CI workflows, env templates, and scaffolding for LangGraph workflows with CrewAI agents and LangChain tools."
Prompt 2 — Core Backend Implementation
"Implement the FastAPI backend: roles/candidates/profiles/screens/interviews/schedules/offers/audits/reports models; resume/JD parsing; embeddings into pgvector; hybrid retrieval; scheduler endpoints; JWT + RBAC + RLS; WebSockets for pipeline and scheduling; logging/OTel; integrations for ATS, calendars, email, storage, and e sign."
Prompt 3 — Frontend Components & UI
"Build the Next.js UI: Pipeline Board, JD Studio (inclusive checker), Talent Pool search, Screening Console with competencies heatmap, Scheduler, Interview Room with rubrics and bias nudges, Decision & Offer, Compliance Hub with EEO/adverse impact dashboards. Ensure dark/light themes and WCAG 2.1 AA."
Prompt 4 — AI Integration & Features
"Wire LangGraph flows (intake → source → screen → schedule → interview → decide → offer) using CrewAI agents (Sourcer, Screener, Scheduler, Offer Analyst) and LangChain retrievers over JDs/competencies/policies/candidate docs. Enforce cite or refuse, anonymization options, fairness constraints, uncertainty bands, and human approval gates for outreach and decisions."
Prompt 5 — Deployment & Optimization
"Prepare for production: Vercel + Render configs, pgvector tuning, Redis rate limits/queues, Playwright e2e tests, load/perf tests, OpenAPI docs, monitoring/alerts (Prometheus/Grafana), backups/PITR, a11y/perf audits, and SLO dashboards for p95 latency and recruiting KPIs (time to screen, schedule success rate, offer acceptance)."
________________________________________
Roadmap (90 Days)
•	Day 30: JD Studio + inclusive checks, candidate import/search, screening MVP.
•	Day 60: Scheduler, interview kits, decision aggregation, offer builder.
•	Day 90: Compliance hub GA, adverse impact monitoring, enterprise SSO/SAML, ATS bi directional sync.
________________________________________
One Slide Pitch
What: A fairness first hiring OS that automates sourcing to offer with evidence and audit trails.
Why it wins: Deterministic orchestration + competency based scoring + RAG grounded rationales.
Who: High growth teams, enterprise TA, RPOs, and internal mobility programs.
CTA: “Hire faster. Hire fair.”





FOLLOW THIS 8 STEP PLAN TO PREPARE THE INFRASTRUCTURE
-----------------------------------------------------

# 🚀 Claude Fullstack Repo Prep – Optimized 8 Step Plan

  
The goal: build an extensive frontend + backend scaffold so Claude Code only has to finish ~20% of the work.  
Each step must be **completed ** before advancing  (this is important).
IMPORTANT: YOU ARE BUILDING ONLY THE INFRASTRUCTURE OF THE APPLICATION NOT THE APPLICATION ITSELF !!!. FOLLOW THE STEPS IN NUMERICAL ORDER !!! starting from step 1.
You are doing the groundwork for the application, including setting up the folder structure, configuration files, and any necessary boilerplate code.
IMPORTANT: the checklist in each step has to be checked off 100% before moving to the next step. And always provide comments to your code blocks so that even a non-tech person can understand what you have done.

---

## STEP 1 — Build the Rich Infrastructure
Create a **deep scaffold** for both frontend and backend so Claude code can recognize the architecture immediately.

- Build a **frontend app shell** with routing, placeholder pages, components, and styling setup.  
- Build a **backend app shell** with API structure, health endpoint, and config in place.  
- Include `REPO_MAP.md`, `API_SPEC.md`, and a draft `CLAUDE.md` in the `docs/` folder.  (create the docs folder if it does not  already exist)
- Add **TODO markers and folder-level `_INSTRUCTIONS.md`** files so Claude knows exactly where to add logic.

**Deliverables**
- Frontend app shell with routing, placeholder pages, components, and styling setup  
- Backend app shell with API structure, health endpoint, and config  
- `docs/REPO_MAP.md`, `docs/API_SPEC.md` (stub), and draft `docs/CLAUDE.md`  
- TODO markers + folder-level `_INSTRUCTIONS.md` files  

**Checklist**
- [ ] Frontend scaffold built  
- [ ] Backend scaffold built 
- [ ] Docs folder created with drafts (`REPO_MAP.md`, `API_SPEC.md`, `CLAUDE.md`)  
- [ ] TODO markers and `_INSTRUCTIONS.md` stubs in place  

---

## STEP 2 — Enrich the Scaffold
If the repo looks shallow, enrich it so Claude needs fewer leaps of imagination.  

Add:
- Sample frontend routes and components (`/`, `/about`, `/dashboard`)  
- Domain model stubs and types/interfaces  
- Mock data + fixtures for UI flows  
- README files with quick run instructions for both frontend and backend  
- Instructions embedded in folders (e.g. `CLAUDE_TASK: …`)

**Deliverables**
- Sample routes and pages (`/`, `/about`, `/dashboard`)  
- Domain model stubs and type definitions  
- Mock data and fixtures for UI flows  
- README files for frontend and backend with run instructions  
- Folder-level instructions (`_INSTRUCTIONS.md`)  

**Checklist**
- [ ] At least 2–3 sample routes/pages exist  
- [ ] Domain types/interfaces stubbed out  
- [ ] Mock data + fixtures included  
- [ ] README_FRONTEND.md and README_BACKEND.md added  
- [ ] Each folder has `_INSTRUCTIONS.md` where relevant 

---

## STEP 3 — Audit for Alignment
Check that the scaffold actually matches the product brief, tech specs, and UX /UI goals.
Add additional UI/UX elements (if needed) to make the application visually appealing (and update the design requirements after that)

- Do navigation and pages reflect the product’s main flows?  
- Do API endpoints match the UI needs?  
- Is the chosen tech stack consistent (no unused or conflicting libraries)?  
- Is the UX direction reflected (design tokens, layout, component stubs)?

**Deliverables**
- Alignment review across Product ↔ UI/UX ↔ Tech  
- Identify any missing flows, mismatched libraries, or conflicting instructions  

**Checklist**
- [ ] Navigation structure matches product journeys  
- [ ] Components/pages map to required features  
- [ ] API endpoints cover MVP needs  
- [ ] No contradictory or unused technologies  

---

## STEP 4 — Document the Architecture
Now make the docs **Claude-ready**:

- **REPO_MAP.md**: Full repo breakdown with roles of each folder  
- **API_SPEC.md**: Endpoints, payloads, error handling  
- **CLAUDE.md**: Editing rules, coding conventions, AI collaboration guidelines  

These three files are the **context backbone** Claude will use to understand the repo.

**Deliverables**
- `REPO_MAP.md`: full repo breakdown with folder purposes  
- `API_SPEC.md`: endpoints, models, error conventions  
- `CLAUDE.md`: collaboration rules, editing boundaries  

**Checklist**
- [ ] REPO_MAP.md fully describes structure  
- [ ] API_SPEC.md covers all MVP endpoints and schemas  
- [ ] CLAUDE.md includes project overview, editing rules, examples  

---

## STEP 5 — Improve the Prompt
Enhance the prompt (in `docs/PROMPT_DECLARATION.md`) with details Claude needs:

- FE/BE boundaries and data contracts  
- UX guidelines (states, accessibility, interaction patterns)  
- Performance budgets (bundle size, API latency)  
- Security constraints (auth, rate limits, PII handling)  
- Testing expectations (unit, integration, end-to-end)

**Deliverables**
- FE/BE boundaries and contracts  
- UX guidelines (states, accessibility, patterns)  
- Performance budgets (bundle size, latency targets)  
- Security constraints (auth, PII, rate limits)  
- Testing expectations  

**Checklist**
- [ ] Prompt includes FE/BE division of responsibility  
- [ ] UX principles and design tokens specified  
- [ ] Performance/security/testing requirements added  
- [ ] Prompt is concrete and actionable for Claude  

---

## STEP 6 — Expert Audit of the Prompt
Now do a **meticulous audit** of the one-page prompt declaration.

- Add Frontend Architecture, Backend Architecture, Design requirements, Core Integrations, Success Criteria, Implementation Guidelines and Security & Compliance categories from this Project Brief to the prompt declaration.
- Remove inconsistencies, duplicates, or unused technologies  
- Ensure Tech Stack → Product → Scaffold alignment (no mismatches)  
- Add UI/UX details that make the product visually appealing and usable  
- Double-check frontend and backend folders are ready  
- Confirm editing boundaries are clear (what Claude can/can’t touch)  
- Make the declaration **battle-tested and handoff-ready**

**Deliverables**
- Remove inconsistencies/duplicates  
- Ensure stack ↔ product ↔ scaffold alignment  
- Add UI/UX and accessibility details  
- Clarify file boundaries (editable vs do-not-touch)  
- Confirm prompt uses Claude-friendly syntax  

**Checklist**
- [ ] No unused or contradictory tech remains  
- [ ] UI/UX directives are product-specific and sufficient  
- [ ] Editing boundaries explicitly defined  
- [ ] Prompt syntax uses clear, imperative instructions  

---

## STEP 7 — Bird’s-Eye Repo Review
Do a quick top-level scan for missing pieces:

- All folders contain either code or `_INSTRUCTIONS.md`  
- `.env.example` files exist for both frontend and backend  
- CI/CD config is present and not trivially broken  
- Run scripts (`npm run dev`, `uvicorn …`) work end-to-end  
- No orphan TODOs without clear ownership

**Deliverables**
- Verify all core files exist  
- Confirm environment, CI, and scripts work end-to-end  

**Checklist**
- [ ] Every folder has code or `_INSTRUCTIONS.md`  
- [ ] `.env.example` present for both frontend and backend  
- [ ] CI pipeline triggers and passes basic checks  
- [ ] Dev script (`scripts/dev.sh`) runs both FE and BE  

---

## STEP 8 — Finalize CLAUDE.md
This is where Claude gets its **onboarding pack**. Make sure `CLAUDE.md` includes:

- **Project Overview**: one-paragraph purpose, stack, goals, target users  
- **Folder & File Structure**: what’s editable vs do-not-touch  
- **Coding Conventions**: style guides, naming rules, commenting expectations  
- **AI Collaboration Rules**: response format, edit rules, ambiguity handling  
- **Editing Rules**: full-file vs patches, locked files  
- **Dependencies & Setup**: frameworks, services, env vars  
- **Workflow & Tools**: how to run locally, FE/BE boundary, deployment notes  
- **Contextual Knowledge**: product quirks, domain rules, business logic caveats  
- **Examples**: good vs bad AI answer

**Deliverables**
- Project overview (purpose, stack, goals, users)  
- Folder & file structure with editable vs do-not-touch  
- Coding conventions (style, naming, commenting)  
- AI collaboration rules (response style, edit rules, ambiguity handling)  
- Dependencies and setup instructions  
- Workflow, deployment notes, contextual knowledge  
- Good vs bad answer examples  
- Fill out all the missing information in the CLAUDE.md file

**Checklist**
- [ ] Project overview section filled in  
- [ ] File boundaries clearly defined  
- [ ] Coding/style conventions included  
- [ ] AI collaboration & editing rules written  
- [ ] Dependencies & env notes covered  
- [ ] Workflow & deployment info added  
- [ ] Contextual knowledge documented  
- [ ] Good vs bad examples included  
- [ ] CLAUDE.md file does not miss any important information

---

# ✅ Outcome
When this 8-step plan is followed:
- The repo is a **rich, opinionated scaffold** (80% done).  
- Docs give Claude **clear boundaries + context**.  
- The one-page prompt is **battle-tested** and aligned.  
- Claude Code can safely and efficiently generate the missing 20%.  












