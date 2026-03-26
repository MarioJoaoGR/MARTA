
from dataclasses_json.utils import _hasargs
from typing import List, Tuple

def test_none_input():
    class MyType(Tuple): pass
    my_instance = MyType([1, 2])
    
    assert not _hasargs(int, 'a')  # False, because 'a' is not an int.
    assert _hasargs(List[int], 'a', 'b')  # True, since both 'a' and 'b' are in List[int].

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        class MyType(Tuple): pass
        my_instance = MyType([1, 2])
    
        assert not _hasargs(int, 'a')  # False, because 'a' is not an int.
>       assert _hasargs(List[int], 'a', 'b')  # True, since both 'a' and 'b' are in List[int].
E       AssertionError: assert False
E        +  where False = _hasargs(typing.List[int], 'a', 'b')

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_none_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__hasargs_3_test_none_input.py::test_none_input
============================== 1 failed in 0.04s ===============================
"""