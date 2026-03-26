
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    mapped_lazy = lazy.map(lambda x: x * 2)
    result = mapped_lazy.fold()
    
    assert result == 100

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_map_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_valid_input.py:10:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""