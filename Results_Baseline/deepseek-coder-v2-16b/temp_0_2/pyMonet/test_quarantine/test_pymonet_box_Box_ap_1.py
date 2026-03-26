
import pytest
from pymonet.box import Box

# Test cases for the Lazy class
def test_lazy_initialization():
    def identity(x): return x
    lazy = Box(identity)  # Create a Box object with an identity function
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_1.py .F                    [100%]

=================================== FAILURES ===================================
__________________________ test_lazy_applies_function __________________________

    def test_lazy_applies_function():
        def add_one(x): return x + 1
        lazy_add_one = Box(add_one)
    
        def multiply_by_two(x): return x * 2
        lazy_multiply_by_two = Box(multiply_by_two)
    
>       result = lazy_add_one.ap(lazy_multiply_by_two)

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_1.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/box.py:57: in ap
    return applicative.map(self.value)
pyMonet/pymonet/box.py:35: in map
    return Box(mapper(self.value))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = <function test_lazy_applies_function.<locals>.multiply_by_two at 0x7f013f5b1940>

>   def add_one(x): return x + 1
E   TypeError: unsupported operand type(s) for +: 'function' and 'int'

pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_1.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_ap_1.py::test_lazy_applies_function
========================= 1 failed, 1 passed in 0.06s ==========================
"""