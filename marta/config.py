class Config:
    need_extract_type: bool = False
    run_benchmark: bool = False
    # Se definido (via --output_dir), TODOS os outputs (Test4DT_tests, test_quarantine,
    # caches, run_results, react_history.txt) vão para {output_dir}/{project_name}/
    # em vez de poluírem o source. None = comportamento legacy.
    output_dir: str = None

config = Config()