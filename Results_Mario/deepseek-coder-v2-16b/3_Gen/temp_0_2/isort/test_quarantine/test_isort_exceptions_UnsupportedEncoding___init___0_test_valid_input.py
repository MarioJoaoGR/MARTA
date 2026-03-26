
import pytest
from isort.exceptions import UnsupportedEncoding
from pathlib import Path

def test_valid_input():
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding("valid_file.txt")
    
    assert str(excinfo.value) == "Unknown or unsupported encoding in valid_file.txt"
    assert isinstance(excinfo.value.filename, Path), f"Expected filename to be a Path but got {type(excinfo.value.filename)}"

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

isort/Test4DT_tests/test_isort_exceptions_UnsupportedEncoding___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with pytest.raises(UnsupportedEncoding) as excinfo:
            raise UnsupportedEncoding("valid_file.txt")
    
        assert str(excinfo.value) == "Unknown or unsupported encoding in valid_file.txt"
>       assert isinstance(excinfo.value.filename, Path), f"Expected filename to be a Path but got {type(excinfo.value.filename)}"
E       AssertionError: Expected filename to be a Path but got <class 'str'>
E       assert False
E        +  where False = isinstance('valid_file.txt', Path)
E        +    where 'valid_file.txt' = UnsupportedEncoding('Unknown or unsupported encoding in valid_file.txt').filename
E        +      where UnsupportedEncoding('Unknown or unsupported encoding in valid_file.txt') = <ExceptionInfo UnsupportedEncoding('Unknown or unsupported encoding in valid_file.txt') tblen=1>.value

isort/Test4DT_tests/test_isort_exceptions_UnsupportedEncoding___init___0_test_valid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_UnsupportedEncoding___init___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""