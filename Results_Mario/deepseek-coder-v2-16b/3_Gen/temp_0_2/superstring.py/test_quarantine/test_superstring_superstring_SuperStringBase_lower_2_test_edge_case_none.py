
from unittest.mock import patch
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

class TestSuperStringBase:
    @patch('superstring.superstring.SuperStringBase.length', return_value=SUPERSTRING_MINIMAL_LENGTH - 1)
    def test_edge_case_none(self, mock_length):
        with pytest.raises(TypeError):
            s = SuperStringBase()
            lower_str = s.lower()

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_2_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
___________________ TestSuperStringBase.test_edge_case_none ____________________

self = <Test4DT_tests.test_superstring_superstring_SuperStringBase_lower_2_test_edge_case_none.TestSuperStringBase object at 0x7fc27e258a10>
mock_length = <MagicMock name='length' id='140473320386832'>

    @patch('superstring.superstring.SuperStringBase.length', return_value=SUPERSTRING_MINIMAL_LENGTH - 1)
    def test_edge_case_none(self, mock_length):
        with pytest.raises(TypeError):
            s = SuperStringBase()
>           lower_str = s.lower()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_2_test_edge_case_none.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringBase object at 0x7fc27f1356d0>

    def lower(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
>           return SuperString(self.to_printable().lower())
E           AttributeError: 'NoneType' object has no attribute 'lower'

superstring.py/superstring/superstring.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_lower_2_test_edge_case_none.py::TestSuperStringBase::test_edge_case_none
============================== 1 failed in 0.05s ===============================
"""