
import pytest
from pymonet.lazy import Lazy

def test_bind():
    def add_one(x):
        return Lazy(lambda y: y + 1)(x).bind(lambda x: Lazy(lambda y: y * y)(x))
    
    lazy = Lazy(add_one)
    result = lazy.fold(5)
    assert result == 36, "Expected the result of square(6), which is 36"

def test_bind_multiple():
    def add_one_then_square(x):
        return Lazy(lambda y: y + 1)(x).bind(lambda x: Lazy(lambda y: y * y)(x)).bind(lambda x: Lazy(lambda y: y + 2)(x))
    
    lazy = Lazy(add_one_then_square)
    result = lazy.fold(5)
    assert result == 49, "Expected the result of (6^2)+2, which is 38"

def test_fold():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    with pytest.raises(TypeError):
        lazy.fold()
    
    result = lazy.fold(5)
    assert result == 25, "Expected the result of square(5), which is 25"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_bind_0_test_edge_cases
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:7:15: E1102: Lazy(lambda y: y + 1) is not callable (not-callable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:7:55: E1102: Lazy(lambda y: y * y) is not callable (not-callable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:10:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:15:15: E1102: Lazy(lambda y: y + 1) is not callable (not-callable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:15:55: E1102: Lazy(lambda y: y * y) is not callable (not-callable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:15:96: E1102: Lazy(lambda y: y + 2) is not callable (not-callable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:18:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:27:8: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_bind_0_test_edge_cases.py:29:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""