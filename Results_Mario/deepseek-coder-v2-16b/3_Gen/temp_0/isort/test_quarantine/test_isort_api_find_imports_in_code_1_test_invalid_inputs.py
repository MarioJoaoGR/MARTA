
from isort.api import find_imports_in_code, Config, DEFAULT_CONFIG
from io import StringIO
from pathlib import Path
from typing import Any, Iterator
import pytest

@pytest.mark.parametrize("unique", [False, True])
def test_find_imports_in_code(unique):
    code = """
    from isort import DEFAULT_CONFIG
    from some_module import SomeClass
    """
    expected_imports = [
        "isort.DEFAULT_CONFIG",
        "some_module.SomeClass"
    ]
    
    result = list(find_imports_in_code(code, unique=unique))
    assert len(result) == 2
    for imp in result:
        assert str(imp) in expected_imports

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_invalid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_find_imports_in_code[False] _______________________

unique = False

    @pytest.mark.parametrize("unique", [False, True])
    def test_find_imports_in_code(unique):
        code = """
        from isort import DEFAULT_CONFIG
        from some_module import SomeClass
        """
        expected_imports = [
            "isort.DEFAULT_CONFIG",
            "some_module.SomeClass"
        ]
    
        result = list(find_imports_in_code(code, unique=unique))
        assert len(result) == 2
        for imp in result:
>           assert str(imp) in expected_imports
E           AssertionError: assert ':2 indented from isort import DEFAULT_CONFIG' in ['isort.DEFAULT_CONFIG', 'some_module.SomeClass']
E            +  where ':2 indented from isort import DEFAULT_CONFIG' = str(Import(line_number=2, indented=True, module='isort', attribute='DEFAULT_CONFIG', alias=None, cimport=False, file_path=None))

isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_invalid_inputs.py:22: AssertionError
_______________________ test_find_imports_in_code[True] ________________________

unique = True

    @pytest.mark.parametrize("unique", [False, True])
    def test_find_imports_in_code(unique):
        code = """
        from isort import DEFAULT_CONFIG
        from some_module import SomeClass
        """
        expected_imports = [
            "isort.DEFAULT_CONFIG",
            "some_module.SomeClass"
        ]
    
        result = list(find_imports_in_code(code, unique=unique))
        assert len(result) == 2
        for imp in result:
>           assert str(imp) in expected_imports
E           AssertionError: assert ':2 indented from isort import DEFAULT_CONFIG' in ['isort.DEFAULT_CONFIG', 'some_module.SomeClass']
E            +  where ':2 indented from isort import DEFAULT_CONFIG' = str(Import(line_number=2, indented=True, module='isort', attribute='DEFAULT_CONFIG', alias=None, cimport=False, file_path=None))

isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_invalid_inputs.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_invalid_inputs.py::test_find_imports_in_code[False]
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_code_1_test_invalid_inputs.py::test_find_imports_in_code[True]
============================== 2 failed in 0.11s ===============================
"""