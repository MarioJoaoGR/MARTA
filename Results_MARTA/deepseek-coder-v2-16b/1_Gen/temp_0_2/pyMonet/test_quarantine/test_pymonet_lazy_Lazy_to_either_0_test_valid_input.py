
from pymonet.lazy import Lazy
from pymonet.either import Right
import pytest

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    either_instance = lazy.to_either()
    
    assert isinstance(either_instance, Right)
    assert either_instance.value == 25  # Assuming the input is 5 for testing purposes

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

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def square(x):
            return x * x
    
        lazy = Lazy(square)
>       either_instance = lazy.to_either()

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/lazy.py:126: in to_either
    return Right(self.get(*args))
pyMonet/pymonet/lazy.py:104: in get
    return self._compute_value(*args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pymonet.lazy.Lazy object at 0x7eff780afd10>, args = ()

    def _compute_value(self, *args):
        self.is_evaluated = True
>       self.value = self.constructor_fn(*args)
E       TypeError: test_valid_input.<locals>.square() missing 1 required positional argument: 'x'

pyMonet/pymonet/lazy.py:52: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_either_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""