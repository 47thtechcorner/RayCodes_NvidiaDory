import os
import ollama

def query_dory(system_prompt: str, user_prompt: str) -> str:
    response = ollama.chat(
        model="dory",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        options={"temperature": 0.2, "num_ctx": 32768}
    )
    return response["message"]["content"]

def task1_codebase_refactor():
    print("[1/3] Running Task 1: Codebase Refactor & Bug Auditor...")
    with open("inputs/task1_codebase_refactor_input.py", "r", encoding="utf-8") as f:
        code_input = f.read()

    sys_prompt = "Audit this code for concurrency deadlocks. Return an analysis summary, then the refactored code."
    response_text = query_dory(sys_prompt, code_input)

    parts = response_text.split("```python")
    analysis = parts[0].strip()
    refactored = parts[1].split("```")[0].strip() if len(parts) > 1 else response_text

    with open("templates/task1_codebase_refactor_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    rendered = template.replace("{{audit_summary}}", analysis).replace("{{refactored_code}}", refactored)
    with open("outputs/task1_codebase_refactor_diff.html", "w", encoding="utf-8") as f:
        f.write(rendered)
    print(" -> Saved: outputs/task1_codebase_refactor_diff.html")

def task2_web_scraper():
    print("[2/3] Running Task 2: Adaptive-Latency Web Scraper & Formatter...")
    with open("inputs/task2_messy_web_page.html", "r", encoding="utf-8") as f:
        html_input = f.read()

    # Phase 1: High-speed noise filtering
    sys_phase1 = "Strip all web noise and script tags. Extract raw GPU pricing lines."
    triage_text = query_dory(sys_phase1, html_input)

    # Phase 2: Dynamic summary and schema structuring
    summary_prompt = "Summarize the available cloud GPU offerings in 1 concise sentence."
    summary_text = query_dory(summary_prompt, triage_text)

    sys_phase2 = "Format this GPU data into a clean markdown table with SKU, GPU Model, Memory, Price, and Availability."
    structured_data = query_dory(sys_phase2, triage_text)

    with open("templates/task2_web_scraper_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    rendered = template.replace("{{executive_summary}}", summary_text).replace("{{structured_catalog}}", structured_data)
    with open("outputs/task2_web_scraper_dashboard.html", "w", encoding="utf-8") as f:
        f.write(rendered)
    print(" -> Saved: outputs/task2_web_scraper_dashboard.html")

def task3_multi_agent_swarm():
    print("[3/3] Running Task 3: Local Multi-Agent Swarm with Dynamic IQ...")
    with open("inputs/task3_system_migration_brief.txt", "r", encoding="utf-8") as f:
        brief_input = f.read()

    # Agent 1: Coordinator (Rapid roadmap planning)
    agent1_prompt = "Create a concise 4-phase cloud migration roadmap for this project brief."
    coord_plan = query_dory(agent1_prompt, brief_input)

    # Agent 2: Deep Security Auditor (SOC2 / HIPAA verification)
    agent2_prompt = "Audit this migration plan against SOC2 and HIPAA zero-trust compliance standards."
    audit_input = f"Brief:\n{brief_input}\n\nProposed Plan:\n{coord_plan}"
    audit_plan = query_dory(agent2_prompt, audit_input)

    with open("templates/task3_multi_agent_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    rendered = template.replace("{{coordinator_output}}", coord_plan).replace("{{auditor_output}}", audit_plan)
    with open("outputs/task3_multi_agent_blueprint.html", "w", encoding="utf-8") as f:
        f.write(rendered)
    print(" -> Saved: outputs/task3_multi_agent_blueprint.html")

def main():
    os.makedirs("outputs", exist_ok=True)
    task1_codebase_refactor()
    task2_web_scraper()
    task3_multi_agent_swarm()
    print("\n✅ All 3 production workflows completed successfully!")

if __name__ == "__main__":
    main()
