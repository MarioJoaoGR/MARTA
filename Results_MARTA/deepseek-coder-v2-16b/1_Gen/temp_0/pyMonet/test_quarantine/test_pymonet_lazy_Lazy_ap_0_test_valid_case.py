
from pymonet.lazy import Lazy

def test_valid_case():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    assert not lazy.is_evaluated
    result = lazy.fold()
    assert lazy.is_evaluated
    assert result == 25

    def add(x, y):
        return x + y
    
    lazy1 = Lazy(lambda x: x * 2)
    lazy2 = Lazy(add)
    applied_lazy = lazy1.ap(lazy2)
    assert not applied_lazy.is_evaluated
    result = applied_lazy.fold()
    assert applied_lazy.is_evaluated
    assert result == 14

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_ap_0_test_valid_case
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_valid_case.py:10:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_ap_0_test_valid_case.py:21:13: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""