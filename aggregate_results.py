import os
import json
import re
import csv
import xml.etree.ElementTree as ET
from pathlib import Path

def parse_run_results(file_path):
    """Safely parse run_results.json, handling potential formatting issues."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # If the file has trailing comma/garbage, this helps clean it up
            if content.endswith(', "coverage": [{}]}'):
                content = content.replace(', "coverage": [{}]}', '}')
            
            data = json.loads(content)
            
            total_time = data.get("time", 0)
            llm_time = data.get("times", {}).get("run_0", 0)
            tests_pass = data.get("assertion_pass", 0)
            syntax_errs = data.get("first_syntax_error", 0)
            
            # Aggregate hallucinated errors
            err_types = data.get("assertion_error_types", {})
            hallucinated = err_types.get("Failed", 0) + err_types.get("AssertionError", 0) + err_types.get("TypeError", 0)
            
            return total_time, llm_time, tests_pass, syntax_errs, hallucinated
    except Exception as e:
        print(f"  [Warning] Could not parse {file_path}: {e}")
        return 0, 0, 0, 0, 0

def parse_coverage(file_path):
    """Parse coverage.json for statement and branch coverage."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            totals = data.get("totals", {})
            
            stmt_cov = totals.get("percent_covered", 0)
            missing_stmts = totals.get("missing_lines", 0)
            
            num_b = totals.get("num_branches", 0)
            cov_b = totals.get("covered_branches", 0)
            branch_cov = (cov_b / num_b * 100) if num_b > 0 else 0
            
            return stmt_cov, branch_cov, missing_stmts
    except Exception as e:
        print(f"  [Warning] Could not parse {file_path}: {e}")
        return 0, 0, 0

def parse_errors(file_path):
    """Parse error.log if it exists to count timeouts."""
    if not os.path.exists(file_path):
        return 0 # No error log means no errors!
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            return len(re.findall(r"Request timed out", text))
    except Exception:
        return 0

def parse_mutation_score(file_path):
    """Parse mutmut_report.xml to calculate the Mutation Score."""
    if not os.path.exists(file_path):
        return "N/A" # Return N/A if mutation testing hasn't been run yet
    
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # In JUnit XML format: 'tests' is the total mutants, 'failures' is survived mutants
        total_mutants = int(root.attrib.get('tests', 0))
        survived_mutants = int(root.attrib.get('failures', 0))
        
        if total_mutants == 0:
            return 0.0
            
        killed_mutants = total_mutants - survived_mutants
        mutation_score = (killed_mutants / total_mutants) * 100
        
        return round(mutation_score, 2)
    except Exception as e:
        print(f"  [Warning] Could not parse mutation XML {file_path}: {e}")
        return "Error"

def generate_csv(root_dir="."):
    root_path = Path(root_dir)
    csv_data = []
    
    # Define CSV Headers
    headers = [
        "Approach", "LLM Model", "Generations", "Temperature", "Program",
        "Statement Cov (%)", "Branch Cov (%)", "Missing Stmts",
        "Total Time (s)", "LLM Time (s)", "Timeouts",
        "Tests Passed", "Syntax Errors", "Hallucinated Asserts", "Mutation Score (%)"
    ]
    csv_data.append(headers)

    print("🔍 Crawling directories for results...")
    
    # --- ALTERAÇÃO AQUI: Lista das pastas que realmente importam ---
    target_folders = ["Results_Baseline", "Results_Mario"]
    
    for folder_name in target_folders:
        folder_path = root_path / folder_name
        
        if not folder_path.exists():
            print(f"  [Aviso] A pasta '{folder_name}' não foi encontrada. A saltar...")
            continue
            
        for cov_file in folder_path.rglob("coverage.json"):
            prog_dir = cov_file.parent
            
            try:
                parts = prog_dir.parts
                program_name = parts[-1]
                temp_str = parts[-2]
                
                # MAGIA DINÂMICA: Verifica se é a estrutura ReAct (Results_Mario) ou Baseline
                if "Gen" in parts[-3]:
                    # É do ReAct (Tem a pasta de gerações)
                    gen_str = parts[-3]
                    llm_model = parts[-4]
                    approach = parts[-5]
                    generations = gen_str.split("_")[0] # "1_Gen" -> "1"
                else:
                    # É da Baseline (A pasta do modelo está logo atrás da temperatura)
                    llm_model = parts[-3]
                    approach = parts[-4]
                    generations = "N/A" # Baseline não tem o conceito de iterações ReAct
                
                temperature = temp_str.replace("temp_", "").replace("_", ".") 
                
                print(f"  -> Processing: {approach} | {program_name} | Gen: {generations} | Temp: {temperature}")
                
                # Paths to the specific files
                run_results_path = prog_dir / "run_results" / f"{program_name}.json"
                error_log_path = prog_dir / "error.log"
                mutmut_xml_path = prog_dir / "mutmut_report.xml"
                
                # Parse data
                stmt_cov, branch_cov, missing_stmts = parse_coverage(cov_file)
                timeouts = parse_errors(error_log_path)
                mutation_score = parse_mutation_score(mutmut_xml_path)
                
                if run_results_path.exists():
                    total_time, llm_time, tests_pass, syntax_errs, hallucinated = parse_run_results(run_results_path)
                else:
                    print(f"  [Warning] Missing run results at {run_results_path}")
                    total_time = llm_time = tests_pass = syntax_errs = hallucinated = 0

                # Add to our data list
                csv_data.append([
                    approach, llm_model, generations, temperature, program_name,
                    f"{stmt_cov:.2f}", f"{branch_cov:.2f}", missing_stmts,
                    f"{total_time:.2f}", f"{llm_time:.2f}", timeouts,
                    tests_pass, syntax_errs, hallucinated, mutation_score
                ])
                
            except IndexError:
                print(f"  [Skip] Path structure doesn't match expected hierarchy: {prog_dir}")

    # Write the compiled data to a CSV file
    output_file = "master_results_summary.csv"
    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
        
    print(f"\n✅ Done! Master CSV saved to: {output_file}")

if __name__ == "__main__":
    generate_csv(".")