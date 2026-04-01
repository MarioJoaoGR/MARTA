
import pytest
from pymonet.semigroups import One

def test_invalid_input_type_error():
    one = One(True)  # Create a valid One instance
    
    with pytest.raises(TypeError):
        invalid_one = One("invalid")  # Attempt to create an invalid One instance

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_2_test_invalid_input_type_error.py F [100%]

=================================== FAILURES ===================================
________________________ test_invalid_input_type_error _________________________

    def test_invalid_input_type_error():
        one = One(True)  # Create a valid One instance
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_2_test_invalid_input_type_error.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_One_concat_2_test_invalid_input_type_error.py::test_invalid_input_type_error
============================== 1 failed in 0.06s ===============================
"""