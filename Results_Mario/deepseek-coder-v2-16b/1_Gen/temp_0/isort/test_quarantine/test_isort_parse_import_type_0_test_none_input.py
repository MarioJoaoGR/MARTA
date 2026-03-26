
from isort.parsing import parse_tokens  # Importing from isort.parsing
from isort.config import Config, DEFAULT_CONFIG  # Importing from isort.config

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
************* Module Test4DT_tests.test_isort_parse_import_type_0_test_none_input
isort/Test4DT_tests/test_isort_parse_import_type_0_test_none_input.py:2:0: E0401: Unable to import 'isort.parsing' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_none_input.py:2:0: E0611: No name 'parsing' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_none_input.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_none_input.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""