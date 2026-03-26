
import pytest
from sty.primitive import Register

@pytest.fixture
def register():
    return Register()

def test_valid_case(register):
    # Test that as_dict returns a dictionary with expected keys and values
    register_dict = register.as_dict()
    
    # Check if the returned dictionary contains the expected keys
    assert "is_muted" in register_dict
    assert register_dict["is_muted"] == str(register.is_muted)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

register = <sty.primitive.Register object at 0x103decaf0>

    def test_valid_case(register):
        # Test that as_dict returns a dictionary with expected keys and values
        register_dict = register.as_dict()
    
        # Check if the returned dictionary contains the expected keys
>       assert "is_muted" in register_dict
E       AssertionError: assert 'is_muted' in {}

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.02s ===============================
"""