
import pytest
from flutes.iterator import Range

def test_edge_cases():
    # Test None as an argument
    with pytest.raises(ValueError):
        r = Range()
    
    # Test empty list as an argument
    with pytest.raises(ValueError):
        r = Range([])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None as an argument
        with pytest.raises(ValueError):
            r = Range()
    
        # Test empty list as an argument
        with pytest.raises(ValueError):
>           r = Range([])

flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.Range object at 0x7f7997d3c5d0>, args = ([],)

    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
            raise ValueError("Range should be called the same way as the builtin `range`")
        if len(args) == 1:
            self.l = 0
            self.r = args[0]
            self.step = 1
        else:
            self.l = args[0]
            self.r = args[1]
            self.step = 1 if len(args) == 2 else args[2]
        self.val = self.l
>       self.length = (self.r - self.l) // self.step
E       TypeError: unsupported operand type(s) for -: 'list' and 'int'

flutes/flutes/iterator.py:328: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_Range___init___0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""