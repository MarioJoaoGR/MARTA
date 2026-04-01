
import pytest
from superstring.superstring import SuperStringBase

@pytest.fixture
def setup():
    return SuperStringBase("valid_input")

def test_invalid_input_none(setup):
    with pytest.raises(TypeError):
        setup.lower()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_0_test_invalid_input_none.py E [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_invalid_input_none ___________________

    @pytest.fixture
    def setup():
>       return SuperStringBase("valid_input")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_0_test_invalid_input_none.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_0_test_invalid_input_none.py::test_invalid_input_none
=============================== 1 error in 0.05s ===============================
"""