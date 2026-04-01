
from isort.config import Config, DEFAULT_CONFIG

def import_type(line: str, config: Config = DEFAULT_CONFIG) -> str | None:
    """If the current line is an import line it will return its type (from or straight)"""
    if config.honor_noqa and line.lower().rstrip().endswith("noqa"):
        return None
    if "isort:skip" in line or "isort: skip" in line or "isort: split" in line:
        return None
    if line.startswith(("import ", "cimport ")):
        return "straight"
    if line.startswith("from "):
        return "from"
    return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse_import_type_4_test_error_case_isort_skip
isort/Test4DT_tests/test_isort_parse_import_type_4_test_error_case_isort_skip.py:2:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_4_test_error_case_isort_skip.py:2:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""