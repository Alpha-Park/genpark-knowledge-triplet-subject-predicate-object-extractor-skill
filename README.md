# GenPark AI Agent Skill - Knowledge Triplet SPO Extractor

Extracts formal (Subject, Predicate, Object) relationship triplets from natural language text to populate knowledge graphs.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Unstructured Natural Language Text] --> B[Syntactic Relation Pattern Matcher]
    B --> C[Subject Entity Extractor]
    B --> D[Predicate Normalizer: works_at / founded / lives_in]
    B --> E[Object Entity Extractor]
    C --> F[Canonical SPO Triplet Object]
    D --> F
    E --> F
    F --> G[Insert Directly into Graph Database / Vector Store]
```

## Features
- **Structured Knowledge Distillation**: Converts prose into queryable graph nodes and edges.
- **Zero External Dependencies**: Pure Python standard library `re`.
