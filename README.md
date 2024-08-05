# Piyathon

## Installation

`pip install piyathon`

## How Piyathon works

```mermaid
graph TD
    A[Piyathon Source Code] --> B[Lexical Tokenization]
    B --> C{Token Type}
    C -->|Keyword| D[Translate to Python Keyword]
    C -->|Other| E[Keep Original Token]
    D --> F[Reassemble Tokens]
    E --> F
    F --> G[Python Source Code]
    G --> H[Python Interpreter]
    H --> I[Execution]

    J[Python Source Code] --> K[Lexical Tokenization]
    K --> L{Token Type}
    L -->|Keyword| M[Translate to Thai Keyword]
    L -->|Other| N[Keep Original Token]
    M --> O[Reassemble Tokens]
    N --> O
    O --> P[Piyathon Source Code]
```
