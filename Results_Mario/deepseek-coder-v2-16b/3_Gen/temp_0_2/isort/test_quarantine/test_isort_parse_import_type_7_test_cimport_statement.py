
from isort.parse import Config, DEFAULT_CONFIG

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

# Test cases for import_type function
def test_import_type():
    # Test a straight import statement
    assert import_type("import os") == "straight"
    
    # Test a from import statement
    assert import_type("from math import sin") == "from"
    
    # Test a line with isort:skip comment which should be skipped
    assert import_type("import sys # isort:skip") == None
    
    # Test a line with cimport which should not be ignored by the function
    assert import_type("cimport some_module") == "straight"
    
    # Test a line with honor_noqa set to True but without noqa, it should return None
    config = Config()
    config.honor_noqa = True
    assert import_type("import sys", config) == None
    
    # Test a line with honor_noqa set to False and containing noqa, it should be ignored
    assert import_type("import sys # noqa") == None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_parse_import_type_7_test_cimport_statement.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_import_type _______________________________

    def test_import_type():
        # Test a straight import statement
        assert import_type("import os") == "straight"
    
        # Test a from import statement
        assert import_type("from math import sin") == "from"
    
        # Test a line with isort:skip comment which should be skipped
        assert import_type("import sys # isort:skip") == None
    
        # Test a line with cimport which should not be ignored by the function
        assert import_type("cimport some_module") == "straight"
    
        # Test a line with honor_noqa set to True but without noqa, it should return None
        config = Config()
>       config.honor_noqa = True

isort/Test4DT_tests/test_isort_parse_import_type_7_test_cimport_statement.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.hg', 'buck-out', '.pants.d', '.mypy_cache', 'node...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
name = 'honor_noqa', value = True

>   ???
E   dataclasses.FrozenInstanceError: cannot assign to field 'honor_noqa'

<string>:4: FrozenInstanceError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_import_type_7_test_cimport_statement.py::test_import_type
============================== 1 failed in 0.14s ===============================
"""