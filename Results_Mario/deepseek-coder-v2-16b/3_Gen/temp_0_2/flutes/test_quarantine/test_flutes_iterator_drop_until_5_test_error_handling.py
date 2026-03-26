
import pytest
from flutes.iterator import drop_until

def test_incorrect_predicate():
    with pytest.raises(ValueError):
        list(drop_until(lambda x: x > 5, range(10)))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_drop_until_5_test_error_handling.py F [100%]

=================================== FAILURES ===================================
___________________________ test_incorrect_predicate ___________________________

    def test_incorrect_predicate():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_iterator_drop_until_5_test_error_handling.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_drop_until_5_test_error_handling.py::test_incorrect_predicate
============================== 1 failed in 0.10s ===============================
"""