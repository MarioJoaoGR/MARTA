
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

@pytest.fixture
def setup_superstring():
    return SuperStringBase("a" * (SUPERSTRING_MINIMAL_LENGTH + 1))

def test_valid_input_long_string(setup_superstring):
    assert isinstance(setup_superstring, SuperStringBase)
    assert len(setup_superstring.to_printable()) == SUPERSTRING_MINIMAL_LENGTH + 1
    assert setup_superstring.upper().to_printable() == "A" * (SUPERSTRING_MINIMAL_LENGTH + 1)

def test_short_string():
    short_string = SuperStringBase("a" * SUPERSTRING_MINIMAL_LENGTH)
    assert isinstance(short_string, SuperStringBase)
    assert len(short_string.to_printable()) == SUPERSTRING_MINIMAL_LENGTH
    assert short_string.upper().to_printable() == "A" * SUPERSTRING_MINIMAL_LENGTH

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_upper_0_test_valid_input_long_string.py E [ 50%]
F                                                                        [100%]

==================================== ERRORS ====================================
________________ ERROR at setup of test_valid_input_long_string ________________

    @pytest.fixture
    def setup_superstring():
>       return SuperStringBase("a" * (SUPERSTRING_MINIMAL_LENGTH + 1))
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_upper_0_test_valid_input_long_string.py:7: TypeError
=================================== FAILURES ===================================
______________________________ test_short_string _______________________________

    def test_short_string():
>       short_string = SuperStringBase("a" * SUPERSTRING_MINIMAL_LENGTH)
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_upper_0_test_valid_input_long_string.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_upper_0_test_valid_input_long_string.py::test_short_string
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_upper_0_test_valid_input_long_string.py::test_valid_input_long_string
========================== 1 failed, 1 error in 0.05s ==========================
"""