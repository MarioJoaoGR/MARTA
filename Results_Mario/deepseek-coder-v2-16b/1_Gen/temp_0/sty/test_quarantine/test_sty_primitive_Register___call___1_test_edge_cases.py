
import pytest
from sty import primitive

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code before each test
    register = primitive.Register()
    yield  # This is where the testing happens
    # Teardown code after each test
    register.is_muted = False  # Resetting for next tests if necessary

def test_call_with_one_arg():
    register = primitive.Register()
    assert register(fg=42) == ""
    assert register(bg='red') == "red"

def test_call_with_three_args():
    register = primitive.Register()
    assert register(bg=(102, 49, 42)) == (102, 49, 42)

def test_call_when_muted():
    register = primitive.Register()
    register.is_muted = True
    assert register(fg=42) == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_edge_cases.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_call_with_one_arg ____________________________

    def test_call_with_one_arg():
        register = primitive.Register()
        assert register(fg=42) == ""
>       assert register(bg='red') == "red"
E       AssertionError: assert '' == 'red'
E         
E         - red

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_edge_cases.py:16: AssertionError
__________________________ test_call_with_three_args ___________________________

    def test_call_with_three_args():
        register = primitive.Register()
>       assert register(bg=(102, 49, 42)) == (102, 49, 42)
E       AssertionError: assert '' == (102, 49, 42)
E        +  where '' = <sty.primitive.Register object at 0x1027cbbb0>(bg=(102, 49, 42))

sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_edge_cases.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_edge_cases.py::test_call_with_one_arg
FAILED sty/Test4DT_tests/test_sty_primitive_Register___call___1_test_edge_cases.py::test_call_with_three_args
========================= 2 failed, 1 passed in 0.03s ==========================

"""