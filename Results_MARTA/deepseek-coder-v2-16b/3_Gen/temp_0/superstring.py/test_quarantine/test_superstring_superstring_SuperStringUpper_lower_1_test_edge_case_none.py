
import pytest
from superstring.superstring import SuperStringUpper

def test_edge_case_none():
    """
    Test the edge case where the input string is None.
    """
    str_upper = SuperStringUpper(None)
    with pytest.raises(TypeError):
        lower_str = str_upper.lower()

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        """
        Test the edge case where the input string is None.
        """
        str_upper = SuperStringUpper(None)
        with pytest.raises(TypeError):
>           lower_str = str_upper.lower()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_edge_case_none.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringUpper object at 0x7fafd255b750>

    def lower(self):
>       return self._base.lower()
E       AttributeError: 'NoneType' object has no attribute 'lower'

superstring.py/superstring/superstring.py:170: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""