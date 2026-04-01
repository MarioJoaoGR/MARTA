
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

class TestSuperStringBase:
    def test_invalid_inputs(self):
        obj = SuperStringBase()
        with pytest.raises(ValueError):
            obj.substring(-1)  # Negative index should raise ValueError
        with pytest.raises(ValueError):
            obj.substring(5, 3)  # end_index < start_index should raise ValueError

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
___________________ TestSuperStringBase.test_invalid_inputs ____________________

self = <Test4DT_tests.test_superstring_superstring_SuperStringBase_substring_0_test_invalid_inputs.TestSuperStringBase object at 0x7fbed5bb4850>

    def test_invalid_inputs(self):
        obj = SuperStringBase()
        with pytest.raises(ValueError):
>           obj.substring(-1)  # Negative index should raise ValueError

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringBase object at 0x7fbed5c00610>
start_index = -1, end_index = None

    def substring(self, start_index, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        # TODO: assert that start_index < end_index
        # TODO: what if start_index == end_index
        if start_index == 0 and end_index == self.length():
            return self
>       if end_index - start_index < SUPERSTRING_MINIMAL_LENGTH:
E       TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'

superstring.py/superstring/superstring.py:41: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_invalid_inputs.py::TestSuperStringBase::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""