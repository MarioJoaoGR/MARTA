
from pathlib import Path
from isort.api import find_imports_in_file, Config, DEFAULT_CONFIG
import io
import pytest

@pytest.fixture(scope="module")
def sample_file(tmp_path_factory):
    file_content = """
import os
import sys
from datetime import datetime
from .local_module import some_function
"""
    file_path = tmp_path_factory.mktemp("data") / "test_file.py"
    with open(file_path, 'w') as f:
        f.write(file_content)
    return file_path

def test_find_imports_in_file_valid(sample_file):
    config = Config()  # Assuming DEFAULT_CONFIG is sufficient for this test
    imports = list(find_imports_in_file(sample_file, config=config))
    
    assert len(imports) == 3
    modules = {imp.module for imp in imports}
    assert modules == {'os', 'sys', '.local_module'}
    aliases = {imp.alias for imp in imports if imp.alias}
    assert aliases == set()
    attributes = {imp.attribute for imp in imports if imp.attribute}
    assert attributes == set()

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=native"])

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

isort/Test4DT_tests/test_isort_api_find_imports_in_file_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_______________________ test_find_imports_in_file_valid ________________________

sample_file = PosixPath('/tmp/pytest-of-joaovitorino/pytest-4/data0/test_file.py')

    def test_find_imports_in_file_valid(sample_file):
        config = Config()  # Assuming DEFAULT_CONFIG is sufficient for this test
        imports = list(find_imports_in_file(sample_file, config=config))
    
>       assert len(imports) == 3
E       AssertionError: assert 4 == 3
E        +  where 4 = len([Import(line_number=2, indented=False, module='os', attribute=None, alias=None, cimport=False, file_path=PosixPath('/t..._function', alias=None, cimport=False, file_path=PosixPath('/tmp/pytest-of-joaovitorino/pytest-4/data0/test_file.py'))])

isort/Test4DT_tests/test_isort_api_find_imports_in_file_0_test_valid_inputs.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_file_0_test_valid_inputs.py::test_find_imports_in_file_valid
============================== 1 failed in 0.12s ===============================
"""