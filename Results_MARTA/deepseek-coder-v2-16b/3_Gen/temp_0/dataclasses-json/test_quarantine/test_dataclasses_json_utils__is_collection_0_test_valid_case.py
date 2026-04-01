
import pytest
from dataclasses_json.utils import _is_collection
from typing import Collection

def test_valid_case():
    from collections import deque
    
    my_deque = deque([1, 2, 3])
    assert _is_collection(my_deque) == True
    
    class MyList:
        def __iter__(self):
            yield 1
    
    my_custom_list = MyList()
    assert _is_collection(my_custom_list) == False

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        from collections import deque
    
        my_deque = deque([1, 2, 3])
>       assert _is_collection(my_deque) == True
E       assert False == True
E        +  where False = _is_collection(deque([1, 2, 3]))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_collection_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.03s ===============================
"""