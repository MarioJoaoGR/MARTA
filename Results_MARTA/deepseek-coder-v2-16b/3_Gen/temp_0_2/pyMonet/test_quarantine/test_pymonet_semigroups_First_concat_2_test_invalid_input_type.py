
import pytest
from pymonet.semigroups import First

def test_invalid_input_type():
    with pytest.raises(TypeError):
        f1 = First(1)
        f2 = "not a semigroup"  # Invalid input type
        combined = f1.concat(f2)  # This should raise TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_semigroups_First_concat_2_test_invalid_input_type.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input_type ____________________________

    def test_invalid_input_type():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_semigroups_First_concat_2_test_invalid_input_type.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_First_concat_2_test_invalid_input_type.py::test_invalid_input_type
============================== 1 failed in 0.08s ===============================
"""