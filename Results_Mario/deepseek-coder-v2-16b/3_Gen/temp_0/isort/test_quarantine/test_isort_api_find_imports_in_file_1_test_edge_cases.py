
import pytest
from pathlib import Path
from isort.api import find_imports_in_file, Config

def test_find_imports_in_file():
    # Assuming 'example.py' is in the current directory for this test
    filename = Path('example.py')
    config = Config()  # Initialize a default configuration if needed
    
    with pytest.raises(FileNotFoundError) as excinfo:
        list(find_imports_in_file(filename, config=config))
    
    assert "No such file or directory" in str(excinfo.value), \
           f"Expected a FileNotFoundError for non-existent file, but got {excinfo.value}"

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

isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________ test_find_imports_in_file ___________________________

    def test_find_imports_in_file():
        # Assuming 'example.py' is in the current directory for this test
        filename = Path('example.py')
        config = Config()  # Initialize a default configuration if needed
    
>       with pytest.raises(FileNotFoundError) as excinfo:
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_edge_cases.py:11: Failed
=============================== warnings summary ===============================
Test4DT_tests/test_isort_api_find_imports_in_file_1_test_edge_cases.py::test_find_imports_in_file
  /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_edge_cases.py:12: UserWarning: Unable to parse file example.py due to [Errno 2] No such file or directory: '/projects/F202407648IACDCF2/mario/example.py'
    list(find_imports_in_file(filename, config=config))

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_find_imports_in_file_1_test_edge_cases.py::test_find_imports_in_file
========================= 1 failed, 1 warning in 0.13s =========================
"""