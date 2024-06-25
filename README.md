# ReflectRAG
```

██████  ███████ ███████ ██      ███████  ██████ ████████ ██████   █████   ██████  
██   ██ ██      ██      ██      ██      ██         ██    ██   ██ ██   ██ ██       
██████  █████   █████   ██      █████   ██         ██    ██████  ███████ ██   ███ 
██   ██ ██      ██      ██      ██      ██         ██    ██   ██ ██   ██ ██    ██ 
██   ██ ███████ ██      ███████ ███████  ██████    ██    ██   ██ ██   ██  ██████  

                                  Routing and self-reflection
                                        🦜🕸️LangGraph
```

ReflectRAG is a non-official implementation inspired by the paper [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511). While it doesn't exactly replicate the methods described in the paper, it strives to capture the core concepts and techniques to the best of its ability. ReflectRAG leverages LangChain and LangGraph to build a robust pipeline for intelligent question answering, incorporating self-reflection steps to ensure the accuracy and relevance of the generated responses.

## Project Structure

The project is organized as follows:

```
src/
├── chains
│   ├── answer_grader.py
│   ├── check_hallucination.py
│   ├── get_relevance.py
│   ├── rag_chain.py
│   └── router.py
├── data_input
│   └── 2310.11511v1.pdf
├── graph
│   ├── create_graph.py
│   └── workflow.py
├── main.py
└── utils
    ├── data_models.py
    ├── models.py
    ├── prompts.py
    ├── settings.py
    └── tools.py
```

## Directory Overview

### chains
Contains the core processing chains for the ReflectRAG pipeline:
- `answer_grader.py`: Evaluates the quality and relevance of generated answers.
- `check_hallucination.py`: Checks for hallucinations (fabricated information) in the generated answers.
- `get_relevance.py`: Grades the relevance of retrieved documents.
- `rag_chain.py`: Implements the main retrieval-augmented generation chain.
- `router.py`: Routes the user questions to the appropriate processing chain.

### data_input
This section exclusively accepts PDF files for input data, such as:
- `2310.11511v1.pdf`: Example PDF document used as part of the knowledge base.

### graph
Contains scripts to build and manage the graph structure of the workflow:
- `create_graph.py`: Script to create the LangGraph graph structure.
- `workflow.py`: Defines the overall workflow of the system.

### utils
Utility scripts and modules:
- `data_models.py`: Defines data models used in the chains.
- `models.py`: Contains model (LLMs and Embedding) definitions and configurations.
- `settings.py`: Default Configuration settings for the project.
- `tools.py`: WebSearch and Retriever.
- `prompts.py`: Contains prompt templates for the chains.

### Prompt Templates

The `prompts.py` file contains various prompt templates used for the LLM. Notably, it includes a `routing_system_template` that needs customization before running the application:

```python
routing_system_template = """You are an expert at routing a user question to a vectorstore or websearch.
The vectorstore contains documents related to -here write your data topic-
Use the vectorstore for questions on these topics. For all else, use websearch."""
```

Before running the app, ensure you specify your data topic in the `routing_system_template` to guide the routing system appropriately.

### main.py
The main entry point for the ReflectRAG system.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- LangChain
- LangGraph

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kirouane-Ayoub/ReflectRAG.git
   cd ReflectRAG
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the main script to start the ReflectRAG pipeline:
   ```bash
   python src/main.py
   ```

### Configuration

Models configurations are managed in `src/utils/settings.py`. Adjust the settings according to your environment and requirements.

### Adding New Data

To add new documents to the knowledge base, place them in the `src/data_input` directory .

### Example


1. **Input**: The process starts with a user question (e.g., "What's Self-RAG?").

2. **Routing**: An initial LLM (Large Language Model) determines if the question is related to the system's knowledge base (index) or requires a web search.

3. For index-related questions:
   - **Retrieve Documents**: The system searches its vector store (database) for relevant information.
   - **Grade Documents**: An LLM evaluates the retrieved documents for relevance.
   - **Generate Answer**: If relevant documents are found, another LLM generates an answer.

4. For non-index questions or if no relevant documents are found:
   - **Web Search**: The system performs an online search for information.

5. Answer Generation and Verification:
   - The system generates an answer using the retrieved or searched information.
   - It then performs several self-reflection steps:
     a. Checks for hallucinations (fabricated information)
     b. Verifies if the generated answer actually addresses the question
     c. If issues are found, it may loop back to generate a new answer or perform additional web searches

6. **Final Output**: The system provides the answer if it passes all verification steps.

---

ReflectRAG aims to deliver accurate and reliable answers by combining powerful language models with intelligent routing and self-reflection techniques. We hope you find this project useful and look forward to your contributions!
