
from pymonet.lazy import Lazy

def test_fold():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert lazy.constructor_fn(5) == 25
    result = lazy.fold()
    assert result == 25

def test_map_and_fold():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    mapped_lazy = lazy.map(lambda x: x * 2)
    folded_result = mapped_lazy.fold()
    assert folded_result == 50

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_map_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_cases.py:10:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_cases.py:19:20: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""