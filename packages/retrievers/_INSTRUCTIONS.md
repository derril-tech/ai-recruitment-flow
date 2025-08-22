# Retrievers Package Instructions

## Purpose
This package contains LangChain retrievers for document and data retrieval in the recruitment process.

## Core Retrievers
1. **Resume Retriever**: Extracts and indexes candidate resumes
2. **JD Retriever**: Retrieves job descriptions and requirements
3. **Competency Retriever**: Maps skills and competencies
4. **Policy Retriever**: Retrieves company policies and guidelines
5. **Interview Retriever**: Retrieves interview questions and rubrics

## Development Guidelines
- Use LangChain for document loading and processing
- Implement vector search with pgvector/ChromaDB
- Include proper text chunking and embedding strategies
- Maintain document metadata and source tracking
- Implement hybrid search (keyword + semantic)
- Use proper indexing and retrieval optimization

## Retriever Structure
```
src/
  retrievers/
    resume/
      resume_retriever.ts
      resume_loader.ts
      resume_processor.ts
    jd/
      jd_retriever.ts
      jd_loader.ts
      jd_processor.ts
    competency/
      competency_retriever.ts
      competency_mapper.ts
      competency_indexer.ts
    policy/
      policy_retriever.ts
      policy_loader.ts
      policy_processor.ts
    interview/
      interview_retriever.ts
      interview_loader.ts
      interview_processor.ts
  types/
    retriever_types.ts
    document_types.ts
  utils/
    embedding_utils.ts
    chunking_utils.ts
    search_utils.ts
  index.ts
```

## TODO: Implement Retrievers
- [ ] Resume Retriever (PDF parsing, text extraction, embedding)
- [ ] JD Retriever (job description analysis, requirement extraction)
- [ ] Competency Retriever (skill mapping, ontology integration)
- [ ] Policy Retriever (company policies, compliance guidelines)
- [ ] Interview Retriever (question banks, rubric retrieval)

## Retrieval Capabilities
- **Resume**: PDF parsing, text extraction, skill identification
- **JD**: Requirement analysis, competency mapping, bias detection
- **Competency**: Skill ontology, proficiency scoring, gap analysis
- **Policy**: Compliance guidelines, company policies, legal requirements
- **Interview**: Question generation, rubric creation, bias detection

## Testing Requirements
- Unit tests for each retriever
- Integration tests with vector databases
- Performance testing for retrieval speed
- Accuracy testing for document processing
