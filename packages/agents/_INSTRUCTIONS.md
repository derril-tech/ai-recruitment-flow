# Agents Package Instructions

## Purpose
This package contains CrewAI agents for specialized recruitment tasks.

## Core Agents
1. **Sourcer Agent**: Discovers and evaluates potential candidates
2. **Screener Agent**: Performs initial candidate screening and evaluation
3. **Scheduler Agent**: Manages interview scheduling and coordination
4. **Interview Kit Curator Agent**: Creates role-specific interview questions
5. **Offer Analyst Agent**: Analyzes market data and generates offer recommendations

## Development Guidelines
- Use CrewAI for agent orchestration and collaboration
- Implement proper role definitions and goals for each agent
- Include tools and capabilities for each agent
- Maintain conversation history and context
- Implement proper error handling and fallback mechanisms
- Use structured outputs for agent responses

## Agent Structure
```
src/
  agents/
    sourcer/
      sourcer_agent.ts
      sourcer_tools.ts
      sourcer_prompts.ts
    screener/
      screener_agent.ts
      screener_tools.ts
      screener_prompts.ts
    scheduler/
      scheduler_agent.ts
      scheduler_tools.ts
      scheduler_prompts.ts
    interview_curator/
      curator_agent.ts
      curator_tools.ts
      curator_prompts.ts
    offer_analyst/
      analyst_agent.ts
      analyst_tools.ts
      analyst_prompts.ts
  types/
    agent_types.ts
    tool_types.ts
  utils/
    agent_utils.ts
    prompt_utils.ts
  index.ts
```

## TODO: Implement Agents
- [ ] Sourcer Agent (candidate discovery, evaluation)
- [ ] Screener Agent (initial screening, competency mapping)
- [ ] Scheduler Agent (interview coordination, calendar management)
- [ ] Interview Kit Curator Agent (question generation, rubric creation)
- [ ] Offer Analyst Agent (market analysis, offer recommendations)

## Agent Capabilities
- **Sourcer**: LinkedIn scraping, resume parsing, candidate outreach
- **Screener**: Resume analysis, competency scoring, risk assessment
- **Scheduler**: Calendar integration, timezone handling, conflict resolution
- **Curator**: Question generation, rubric creation, bias detection
- **Analyst**: Market research, compensation analysis, offer optimization

## Testing Requirements
- Unit tests for each agent
- Integration tests for agent collaboration
- Mock external service dependencies
- Performance testing for agent response times
