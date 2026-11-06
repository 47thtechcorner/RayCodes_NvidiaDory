<div align="center">
  <a href="https://youtu.be/7QJz4u0cjsE">
    <img src="https://img.youtube.com/vi/7QJz4u0cjsE/0.jpg" alt="NVIDIA Dory 1.0: This 4B AI Beats 27B Models Without Adding GPU!">
  </a>
  <h3>📺 <a href="https://youtu.be/7QJz4u0cjsE">Watch the full tutorial on YouTube</a></h3>
</div>

# NVIDIA Nemotron-Labs Dory 1.0 (4B)

[![License: OpenMDW-1.1](https://img.shields.io/badge/License-OpenMDW--1.1-green.svg)](https://huggingface.co/cloudnathan5/Dory1.0-4B-GGUF)
[![Model Size: 4B Looped](https://img.shields.io/badge/Architecture-Looped_Transformer_4B-blue.svg)](https://huggingface.co/cloudnathan5/Dory1.0-4B-GGUF)
[![SWE-bench Verified: 61.8%](https://img.shields.io/badge/SWE--bench_Verified-61.8%25-orange.svg)](https://huggingface.co/cloudnathan5/Dory1.0-4B-GGUF)
[![Memory Footprint: 2.43 GB](https://img.shields.io/badge/Local_VRAM-2.43_GB_Q4_K_M-purple.svg)](https://huggingface.co/cloudnathan5/Dory1.0-4B-GGUF)
[![Context Window: 256K SWA](https://img.shields.io/badge/Context-256K_Sliding_Window-cyan.svg)](https://huggingface.co/cloudnathan5/Dory1.0-4B-GGUF)

> "NVIDIA Nemotron-Labs Dory 1.0 (4B) introduces latent-recurrent looped architecture that re-circulates an internal 20-layer block up to 4 times per token. This dynamic compute scaling simulates a 96-layer architecture at the static VRAM footprint of a 4B model, delivering 256K context processing that rivals 27B-class models on local consumer hardware."

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **Offline Codebase Refactor & Bug Auditor** | Latent Recurrent Concurrency & Memory Bug Auditing | Multi-module asynchronous Python codebase with hidden race conditions | Interactive side-by-side visual diff viewer with logic bug triage |
| **Adaptive-Latency Web Scraper & Formatter** | Dual-Phase Elastic Noise Filtering & Structured Schema Extraction | Raw uncurated enterprise web page dump with script tags and DOM clutter | Interactive responsive web intelligence dashboard with verified metrics |
| **Local Multi-Agent Swarm with Dynamic IQ** | Dynamic Dual-Agent Architecture & Governance Orchestration | Multi-tier cloud migration and infrastructure compliance brief | Interactive system architectural blueprint and governance dashboard |

---

## ⚡ Quick Start (Windows PowerShell)

### Step 1: Setup Environment, Download Weights & Register Runtime

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

hf download cloudnathan5/Dory1.0-4B-GGUF Dory1.0-4B-Q4_K_M.gguf --local-dir models

ollama create dory -f Modelfile
```

### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

## 🛡️ Practical Use Cases

- ⚡ **Local Codebase Intelligence**: Ingest full software repositories into native 256K sliding-window context to detect insidious race conditions, resource leaks, and edge-case exceptions without external cloud API fees.
- 🩺 **Adaptive Data Ingestion & Extraction**: Stream massive raw documentation and web DOM dumps at low-depth rapid evaluation, automatically escalating to deep recurrent latent reasoning for high-precision schema structuring.
- 💳 **Resource-Constrained Edge Swarms**: Run multi-agent swarms concurrently on a single 16GB RAM laptop, allocating rapid triage tasks to loop=1 and assigning mission-critical architectural audits to deep loop=4 compute.
- 📊 **High-Density Contract & Regulatory Audit**: Scan 150+ page commercial agreements to uncover buried indemnity liabilities and cross-clause conflicts without context truncation.

---

## 🚀 Future Feature Roadmap

- 🧭 **Dynamic Auto-Loop Heuristic Engine**: Real-time token entropy evaluation to automatically modulate layer recirculation between 1× and 4× based on runtime problem complexity.
- 🛰️ **Distributed Context Sharding**: Multi-GPU pipeline parallelism to expand beyond 256K context across networked workstation nodes.
- 🧪 **Interactive Latent Attention Visualizer**: WebGL-based inspection interface revealing token recirculation paths and hidden latent state activations inside the recurrent block.
- 📦 **Automated CLI Daemon**: System tray service monitoring hardware thermals and battery levels to dynamically constrain reasoning loops for continuous background tasks.

---

### 🏷️ Search Tags
NVIDIA Dory, Dory 1.0, Nemotron Labs, looped transformer, latent reasoning, Ollama Dory, OpenMDW license, small LLM reasoning, Dory GGUF, NVIDIA AI model, local code auditor, NVIDIA Nemotron, Dory vs Gemma, Qwen alternative, Dory vs Qwen, codebase refactor, agent swarm, local AI coding, NVIDIA local AI, Dory benchmark, Dory coding agent, NVIDIA 4B, Nemotron 4B, NVIDIA AI, Dory Ollama, AI reasoning, local coding AI, code refactoring, code auditing, AI coding agent
