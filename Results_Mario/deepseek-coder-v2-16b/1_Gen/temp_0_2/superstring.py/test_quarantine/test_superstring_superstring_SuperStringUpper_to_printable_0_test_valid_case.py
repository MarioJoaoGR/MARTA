
import pytest
from superstring.superstring import SuperStringBase, SuperStringUpper

@pytest.fixture(params=[("Hello, World!", None, "HELLO, WORLD!"), ("", None, ""), ("Python", 1, 4, "YTH")])
def s_t_u(request):
    base = SuperStringBase(*request.param)
    return SuperStringUpper(base)

def test_valid_case(s_t_u):
    assert s_t_u.to_printable() == s_t_u.to_printable().upper()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_case[s_t_u0] ___________________

request = <SubRequest 's_t_u' for <Function test_valid_case[s_t_u0]>>

    @pytest.fixture(params=[("Hello, World!", None, "HELLO, WORLD!"), ("", None, ""), ("Python", 1, 4, "YTH")])
    def s_t_u(request):
>       base = SuperStringBase(*request.param)
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py:7: TypeError
__________________ ERROR at setup of test_valid_case[s_t_u1] ___________________

request = <SubRequest 's_t_u' for <Function test_valid_case[s_t_u1]>>

    @pytest.fixture(params=[("Hello, World!", None, "HELLO, WORLD!"), ("", None, ""), ("Python", 1, 4, "YTH")])
    def s_t_u(request):
>       base = SuperStringBase(*request.param)
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py:7: TypeError
__________________ ERROR at setup of test_valid_case[s_t_u2] ___________________

request = <SubRequest 's_t_u' for <Function test_valid_case[s_t_u2]>>

    @pytest.fixture(params=[("Hello, World!", None, "HELLO, WORLD!"), ("", None, ""), ("Python", 1, 4, "YTH")])
    def s_t_u(request):
>       base = SuperStringBase(*request.param)
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py::test_valid_case[s_t_u0]
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py::test_valid_case[s_t_u1]
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_case.py::test_valid_case[s_t_u2]
============================== 3 errors in 0.05s ===============================
"""