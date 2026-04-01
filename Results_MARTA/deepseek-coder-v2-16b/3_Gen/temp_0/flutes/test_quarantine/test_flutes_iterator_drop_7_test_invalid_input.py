
import pytest
from itertools import count
from typing import Iterable, Iterator, Type
from flutes.iterator import drop

def test_invalid_input():
    n = 'a'
    iterable = count()
    with pytest.raises(TypeError) as excinfo:
        drop(n, iterable)
    assert str(excinfo.value) == "'int' object is not callable"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_drop_7_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        n = 'a'
        iterable = count()
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_iterator_drop_7_test_invalid_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_drop_7_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.11s ===============================
"""