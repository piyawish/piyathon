# How Piyathon works

## Without AST

This diagram illustrates the token-based translation approach employed by Piyathon to convert between standard Python and Piyathon code. By using Thai keywords and function names, Piyathon provides a Thai language interface while maintaining full compatibility with Python's syntax and features.

English

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

Thai

```mermaid
graph TD
    A[โค้ดต้นฉบับปิยะธอน] --> B[การแยกวิเคราะห์คำ]
    B --> C{ประเภทโทเคน}
    C -->|คำสำคัญ| D[แปลเป็นคำสำคัญไพธอน]
    C -->|อื่นๆ| E[คงโทเคนเดิม]
    D --> F[ประกอบโทเคนใหม่]
    E --> F
    F --> G[โค้ดต้นฉบับไพธอน]
    G --> H[ตัวแปลภาษาไพธอน]
    H --> I[การประมวลผล]

    J[โค้ดต้นฉบับไพธอน] --> K[การแยกวิเคราะห์คำ]
    K --> L{ประเภทโทเคน}
    L -->|คำสำคัญ| M[แปลเป็นคำสำคัญไทย]
    L -->|อื่นๆ| N[คงโทเคนเดิม]
    M --> O[ประกอบโทเคนใหม่]
    N --> O
    O --> P[โค้ดต้นฉบับปิยะธอน]
```

## With AST

English

```mermaid
graph TD
    A[Piyathon Source Code] --> B[Lexical Analysis]
    B --> C[Tokenization]
    C --> D[Parsing]
    D --> E[Piyathon AST]
    E --> F{AST Transformation}
    F -->|Node Traversal| G{Keyword Type}
    G -->|Thai| H[Translate to English]
    G -->|Other| I[Keep Original]
    H --> J[Update AST Node]
    I --> J
    J --> K{More Nodes?}
    K -->|Yes| F
    K -->|No| L[Python AST]
    L --> M[Code Generation]
    M --> N[Python Source Code]
    N --> O[Python Interpreter]
    O --> P[Execution]

    Q[Python Source Code] --> R[Lexical Analysis]
    R --> S[Tokenization]
    S --> T[Parsing]
    T --> U[Python AST]
    U --> V{AST Transformation}
    V -->|Node Traversal| W{Keyword Type}
    W -->|English| X[Translate to Thai]
    W -->|Other| Y[Keep Original]
    X --> Z[Update AST Node]
    Y --> Z
    Z --> AA{More Nodes?}
    AA -->|Yes| V
    AA -->|No| AB[Piyathon AST]
    AB --> AC[Code Generation]
    AC --> AD[Piyathon Source Code]
```

Thai

```mermaid
graph TD
    A[โค้ดต้นฉบับ ปิยะธอน] --> B[การวิเคราะห์คำ]
    B --> C[การแบ่งโทเค็น]
    C --> D[การแยกวิเคราะห์]
    D --> E[AST ของ ปิยะธอน]
    E --> F{การแปลง AST}
    F -->|การวนซ้ำโหนด| G{ประเภทคำสำคัญ}
    G -->|ภาษาไทย| H[แปลเป็นภาษาอังกฤษ]
    G -->|อื่นๆ| I[คงเดิม]
    H --> J[อัปเดตโหนด AST]
    I --> J
    J --> K{มีโหนดเหลืออยู่?}
    K -->|ใช่| F
    K -->|ไม่| L[AST ของ Python]
    L --> M[การสร้างโค้ด]
    M --> N[โค้ดต้นฉบับ Python]
    N --> O[ตัวแปลภาษา Python]
    O --> P[การทำงาน]

    Q[โค้ดต้นฉบับ Python] --> R[การวิเคราะห์คำ]
    R --> S[การแบ่งโทเค็น]
    S --> T[การแยกวิเคราะห์]
    T --> U[AST ของ Python]
    U --> V{การแปลง AST}
    V -->|การวนซ้ำโหนด| W{ประเภทคำสำคัญ}
    W -->|ภาษาอังกฤษ| X[แปลเป็นภาษาไทย]
    W -->|อื่นๆ| Y[คงเดิม]
    X --> Z[อัปเดตโหนด AST]
    Y --> Z
    Z --> AA{มีโหนดเหลืออยู่?}
    AA -->|ใช่| V
    AA -->|ไม่| AB[AST ของ ปิยะธอน]
    AB --> AC[การสร้างโค้ด]
    AC --> AD[โค้ดต้นฉบับ ปิยะธอน]
```
