# Workflows Package Instructions

## Purpose
This package contains LangGraph workflows for the recruitment process orchestration.

## Core Workflows
1. **Intake Workflow**: Role creation, JD generation, competency mapping
2. **Sourcing Workflow**: Candidate discovery, deduplication, outreach
3. **Screening Workflow**: AI-powered candidate evaluation and shortlisting
4. **Scheduling Workflow**: Interview coordination and calendar management
5. **Interview Workflow**: Structured interview execution and feedback
6. **Decision Workflow**: Score aggregation and hiring decisions
7. **Offer Workflow**: Offer generation and negotiation

## Development Guidelines
- Use LangGraph for deterministic workflow orchestration
- Implement proper error handling and retry logic
- Include human approval gates where required
- Maintain audit trails for all workflow steps
- Use Zod for input/output validation
- Implement proper state management and persistence

## Workflow Structure
```
src/
  workflows/
    intake/
      intake_workflow.ts
      intake_state.ts
      intake_agents.ts
    sourcing/
      sourcing_workflow.ts
      sourcing_state.ts
      sourcing_agents.ts
    screening/
      screening_workflow.ts
      screening_state.ts
      screening_agents.ts
    scheduling/
      scheduling_workflow.ts
      scheduling_state.ts
      scheduling_agents.ts
    interview/
      interview_workflow.ts
      interview_state.ts
      interview_agents.ts
    decision/
      decision_workflow.ts
      decision_state.ts
      decision_agents.ts
    offer/
      offer_workflow.ts
      offer_state.ts
      offer_agents.ts
  types/
    workflow_types.ts
    state_types.ts
  utils/
    workflow_utils.ts
    validation.ts
  index.ts
```

## TODO: Implement Workflows
- [ ] Intake workflow (role creation, JD generation)
- [ ] Sourcing workflow (candidate discovery, deduplication)
- [ ] Screening workflow (AI evaluation, shortlisting)
- [ ] Scheduling workflow (interview coordination)
- [ ] Interview workflow (structured interviews)
- [ ] Decision workflow (score aggregation)
- [ ] Offer workflow (offer generation)

## Testing Requirements
- Unit tests for each workflow step
- Integration tests for complete workflows
- Mock external service dependencies
- Performance testing for workflow execution time
