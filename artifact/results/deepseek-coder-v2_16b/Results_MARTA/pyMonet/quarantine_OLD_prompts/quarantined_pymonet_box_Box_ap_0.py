
import pytest
from pymonet.box import Box

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_box_Box_ap_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        box = Box(42)
        doubled_box = box.map(lambda x: x * 2)
        assert doubled_box.value == 84
    
        bound_box = box.bind(lambda x: Box(x * 2))
        assert bound_box.value == 84
    
        applicative_box = Box(lambda x: x * 2)
>       applied_box = box.ap(applicative_box)

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_box_Box_ap_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/box.py:57: in ap
    return applicative.map(self.value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.box.Box object at 0x7fea33484a60>, mapper = 42

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

/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/box.py:35: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_box_Box_ap_0.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""