
import pytest
from typing import List, Tuple, Set
from dataclasses_json.utils import _hasargs

# Test cases for _hasargs function
def test_hasargs_with_valid_arguments():
    class ExampleClass1(object): pass
    ExampleClass1.__args__ = (int, str)
    
    assert _hasargs(ExampleClass1, 'int', 'str') == True

def test_hasargs_with_invalid_arguments():
    class ExampleClass2(object): pass
    ExampleClass2.__args__ = (int,)
    
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_hasargs_with_valid_arguments _______________________

    def test_hasargs_with_valid_arguments():
        class ExampleClass1(object): pass
        ExampleClass1.__args__ = (int, str)
    
>       assert _hasargs(ExampleClass1, 'int', 'str') == True
E       AssertionError: assert False == True
E        +  where False = _hasargs(<class 'Test4DT_tests.test_dataclasses_json_utils__hasargs_0.test_hasargs_with_valid_arguments.<locals>.ExampleClass1'>, 'int', 'str')

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_0.py::test_hasargs_with_valid_arguments
========================= 1 failed, 1 passed in 0.02s ==========================

"""