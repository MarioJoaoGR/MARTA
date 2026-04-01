
from pymonet.box import Box

def test_valid_input():
    box = Box(123)
    applicative = Box(lambda x: x + 1)
    
    result = box.ap(applicative)
    
    assert isinstance(result, Box)
    assert result.value == 124

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_valid_input.py F    [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        box = Box(123)
        applicative = Box(lambda x: x + 1)
    
>       result = box.ap(applicative)

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/box.py:57: in ap
    return applicative.map(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.box.Box object at 0x7f0ab8fc38d0>, mapper = 123

    def map(self, mapper: Callable[[T], U]) -> 'Box[U]':
        """
        Take function (A) -> b and applied this function on current box value and returns new box with mapped value.
    
        :param mapper: mapper function
        :type mapper: Function(A) -> B
        :returns: new box with mapped value
        :rtype: Box[B]
        """
>       return Box(mapper(self.value))
E       TypeError: 'int' object is not callable

pyMonet/pymonet/box.py:35: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""