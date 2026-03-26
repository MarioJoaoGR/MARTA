
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    
    # Adding a value to the set should not raise an error since we are only testing invalid input for discard method
    with pytest.raises(KeyError):  # Expecting a KeyError since the value is not in the set
        meta_set.discard(1)  # Attempting to discard a value that is not in the set should raise a KeyError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_discard_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        meta_set = MetaSet()
    
        # Adding a value to the set should not raise an error since we are only testing invalid input for discard method
>       with pytest.raises(KeyError):  # Expecting a KeyError since the value is not in the set
E       Failed: DID NOT RAISE <class 'KeyError'>

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_discard_1_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_discard_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""