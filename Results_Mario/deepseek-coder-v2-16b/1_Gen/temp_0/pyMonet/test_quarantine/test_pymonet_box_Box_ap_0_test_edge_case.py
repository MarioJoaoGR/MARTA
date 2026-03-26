
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    applicative = Box(lambda x: 'default' if x is None else x)
    
    result = box.ap(applicative)
    
    assert result.value == 'default'

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

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_edge_case.py F      [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        box = Box(None)
        applicative = Box(lambda x: 'default' if x is None else x)
    
>       result = box.ap(applicative)

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/box.py:57: in ap
    return applicative.map(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.box.Box object at 0x7fa50fd70c50>, mapper = None

    def map(self, mapper: Callable[[T], U]) -> 'Box[U]':
        """
        Take function (A) -> b and applied this function on current box value and returns new box with mapped value.
    
        :param mapper: mapper function
        :type mapper: Function(A) -> B
        :returns: new box with mapped value
        :rtype: Box[B]
        """
>       return Box(mapper(self.value))
E       TypeError: 'NoneType' object is not callable

pyMonet/pymonet/box.py:35: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""