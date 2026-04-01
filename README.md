# MARTA: A Decoupled Multi-Agent Architecture for Python Test Generation

This repository contains the source code, experimental data, and evaluation scripts for the paper: **"MARTA: A Decoupled Multi-Agent Architecture for Python Test Generation"**.

## 💡 Overview

Automated test generation using Large Language Models (LLMs) often struggles with dynamically typed languages like Python. Monolithic LLMs forced to process massive contexts in a single pass suffer from cognitive overload, leading to hallucinated variables and syntactically invalid code.

**MARTA** addresses these limitations through a decoupled, multi-agent pipeline:
1. **Task Decoupling:** Separates abstract test planning from concrete syntax formulation.
2. **Inner ReAct Loop (Self-Healing):** Utilizes direct `pytest` execution feedback to dynamically debug and fix failing assertions.
3. **Outer Coverage-Driven Loop:** Parses `coverage.py` reports to augment prompts with unexecuted line data, forcing the agents to explore complex edge cases.

## 📂 Repository Structure

Based on the core implementation and evaluation pipeline, the repository is structured as follows:

.
├── test4dt/                      # 🧠 Core MARTA Source Code
│   ├── pycg/                     # Call Graph generation utilities
│   ├── start_react.py            # Main entry point for MARTA (Multi-Agent + ReAct)
│   ├── start.py                  # Main entry point for the Monolithic Baseline
│   ├── message_react.py          # Planner & Assertion Agent prompt constructions
│   ├── testcase_react.py         # Inner ReAct loop and Pytest execution logic
│   ├── coverage_message.py       # Outer Coverage-Driven loop parser
│   ├── react_logger.py           # Execution and repair trace logging
│   ├── gptapi.py                 # LLM API interface
│   └── embedding.py              # Local RAG embedding utilities
├── Results_Baseline/             # 📊 Raw test generation data for the Baseline
├── Results_MARTA/                # 🚀 Raw test generation data for MARTA
├── figures/                      # 🖼️ Output directory for generated PDF charts
├── isort/                        # 📁 Example of a target evaluation project
├── aggregate_results.py          # ⚙️ Script to parse outputs into a CSV summary
├── generate_figures.py           # 📈 Script to generate academic figures
├── master_results_summary.csv    # 📝 Aggregated benchmark results 
├── projects.json                 # 📋 Configuration detailing the 10 target projects
└── requirements.txt              # 📦 Python dependencies

## 🎬 Requirements & Installation

### 1. Install Global Dependencies

Ensure you have Python 3.10+ installed. Clone this repository and install the framework requirements:
pip install -r requirements.txt

### 2. Environment Setup for Target Projects

To properly execute and heal tests, MARTA requires the target Python project (e.g., `isort` or `sty`) to be installed in your environment alongside the core testing utilities:

pip install pytest coverage pytest-json-report mutmut

### 3. Configure API Keys
Create or edit the `.env` file in the root directory to include your LLM API credentials:

OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=your_api_base_url_here
TRANSFORMER_PATH=path_to_local_huggingface_embeddings # If using local RAG


## 🚀 Quick Start (Generating Tests)

Ensure the target project (e.g., `sty`) is available in the root directory. 

**To run MARTA (Multi-Agent + ReAct):**

python -m test4dt.start_react --project_path sty --source_path sty


**To run the Monolithic Baseline:**

python -m test4dt.start --project_path sty --source_path sty


## 📈 Replicating the Paper's Evaluation

**1. Aggregating Raw Data:**
To re-aggregate the raw execution logs into the consolidated CSV:

python aggregate_results.py


**2. Generating Academic Figures:**
To replicate the exact figures used in the paper:

python generate_figures.py
