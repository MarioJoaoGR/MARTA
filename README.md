Peço desculpa, entendo agora. Queres o conteúdo completo e contínuo num único bloco de código Markdown para que possas copiar tudo de uma vez.

Aqui tens o ficheiro `README.md` completo:

```markdown
# MARTA: A Decoupled Multi-Agent Architecture for Python Test Generation

![Architecture Diagram](figures/architecture.png)

This repository contains the source code, experimental data, and evaluation scripts for the paper: **"MARTA: A Decoupled Multi-Agent Architecture for Python Test Generation"**.

## 💡 Overview

Automated test generation using Large Language Models (LLMs) often struggles with dynamically typed languages like Python. When monolithic LLMs are forced to process massive structural contexts in a single pass, they suffer from cognitive overload. This frequently leads to hallucinated variables, non-existent method calls, and syntactically invalid code.

To overcome this bottleneck, we present **MARTA** (Multi-Agent Refinement and Testing Architecture). MARTA addresses these limitations through a decoupled, multi-agent pipeline:

1.  **Task Decoupling:** Separates abstract test planning (QA Lead persona) from concrete syntax formulation (Developer persona).
2.  **Inner ReAct Loop (Self-Healing):** Utilizes direct `pytest` execution feedback to dynamically refine and fix failing assertions before they reach the final suite.
3.  **Outer Coverage-Driven Loop:** Parses intermediate `coverage.py` reports to augment the prompt with unexecuted line data, forcing the agents to explore complex edge cases.

In our comprehensive evaluation across 10 diverse open-source Python projects, MARTA achieved a staggering **9x increase in executable tests** (from 220 to 2,020) compared to a monolithic baseline, while significantly boosting Statement Coverage (up to 65.02%) and Fault-Revealing Capability (Mutation Score of 35.82%).

* Directory `ex-results/` contains the raw experimental data and generated test suites.
* Directory `figures/` contains the Python scripts to replicate the visual data from the paper.

## 🎬 Requirements

### 1. Install dependencies

Ensure you have Python 3.10+ installed. Clone this repository and install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Environment Setup for Target Projects

To properly execute and heal tests, MARTA requires the target Python project to be installed in your environment. You must also install the core testing utilities:

```bash
pip install pytest coverage pytest-json-report
# If running mutation testing:
pip install mutmut 
```

### 3. Configure LLM API Keys

MARTA utilizes external LLM APIs (e.g., DeepSeek-Coder-V2) for agent generation. Create a `.env` file in the root directory and add your API credentials:

```env
LLM_API_KEY=your_api_key_here
LLM_API_BASE=your_api_base_url_here
```

## 🚀 Quick Start

Ensure that the project you want to test can successfully run in your current Python environment. 

To start generating and refining tests for a specific target (e.g., source code located in `src/`), run the following command:

```bash
python -m marta.start --project_path ./my_project --source_path src/ --generations 3 --temperature 0.2
```

* `--generations 3`: Enables the full 3-round outer coverage-driven loop.
* `--temperature 0.2`: Sets the optimal generative entropy for the ReAct self-healing phase.

## 🔥 Experimental Results

The original experimental data, including baseline comparisons and ablation studies, can be viewed in the `ex-results/` directory. Our evaluation was guided by four main Evaluation Objectives (EOs):

### EO1: Assertion Robustness and Executability (Self-Healing)
MARTA completely mitigates the hallucination problem inherent to single-shot generators. By utilizing the inner ReAct loop, MARTA increased the yield of valid, executable tests from a mere 220 (monolithic baseline) to **2,020**, an approximate 800% increase, while drastically reducing syntactically broken assertions.

### EO2: Structural Coverage Maximization
Single-shot generators suffer from "happy path" bias. By explicitly pointing the Planner Agent to unexecuted lines via our outer loop, MARTA actively explores complex branches. On average, MARTA outperformed the baseline by raising Statement Coverage from 58.20% to **65.02%** across 10 diverse repositories.

### EO3: Fault-Revealing Capability (Mutation Score)
High coverage is only useful if assertions are rigorous. Our mutation analysis reveals that MARTA generates highly capable assertions, improving the average mutation score from 27.14% (Baseline) to **35.82%**. In complex projects like `flutes`, the score surged to over 67%.

### EO4: Ablation Study and Temperature Impact
Our ablation study confirms the necessity of both iterative loops. While a single-generation pass ($X=1$) already beats the baseline by leveraging self-healing, running the full coverage-driven setup ($X=3$) nearly doubles the executable test yield and provides a definitive boost to fault detection. Furthermore, a slight temperature increase ($T=0.2$) was proven essential to prevent the ReAct agents from getting stuck in rigid correction loops.
```

