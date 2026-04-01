
import pytest
from pytutils.rand import rand_hex
import random

@pytest.mark.parametrize("input_value, expected", [
    (None, pytest.raises(TypeError, match="rand_hex expects an int for length")),
])
def test_edge_case_none(input_value, expected):
    with expected:
        rand_hex(input_value)

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

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________ test_edge_case_none[None-expected0] ______________________

input_value = None
expected = <_pytest.python_api.RaisesContext object at 0x7fd60e1a7d90>

    @pytest.mark.parametrize("input_value, expected", [
        (None, pytest.raises(TypeError, match="rand_hex expects an int for length")),
    ])
    def test_edge_case_none(input_value, expected):
        with expected:
>           rand_hex(input_value)

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_edge_case_none.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

length = None

    def rand_hex(length=8):
        """
        Create a random hex string of a specific length performantly.
    
        :param int length: length of hex string to generate
        :return: random hex string
        """
>       return '%0{}x'.format(length) % random.randrange(16**length)
E       TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'NoneType'

pytutils/pytutils/rand.py:11: TypeError

During handling of the above exception, another exception occurred:

input_value = None
expected = <_pytest.python_api.RaisesContext object at 0x7fd60e1a7d90>

    @pytest.mark.parametrize("input_value, expected", [
        (None, pytest.raises(TypeError, match="rand_hex expects an int for length")),
    ])
    def test_edge_case_none(input_value, expected):
>       with expected:
E       AssertionError: Regex pattern did not match.
E        Regex: 'rand_hex expects an int for length'
E        Input: "unsupported operand type(s) for ** or pow(): 'int' and 'NoneType'"

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_edge_case_none.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_5_test_edge_case_none.py::test_edge_case_none[None-expected0]
============================== 1 failed in 0.07s ===============================
"""