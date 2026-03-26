
import pytest
from pytutils.props import lazyclassproperty

def lazyclassproperty(fn):
    """
    Lazy/Cached class property.
    """
    attr_name = '_lazy_' + fn.__name__

    @classmethod
    def _lazyclassprop(cls):
        if not hasattr(cls, attr_name):
            setattr(cls, attr_name, fn(cls))
        return getattr(cls, attr_name)

    return property(_lazyclassprop)

# Test case for the edge case scenario
def test_edge_case(caplog):
    class MyClass:
        @lazyclassproperty
        def expensive_calculation(cls):
            print("Calculating...")
            return sum(range(1000))
    
    # Capture log messages to check if the calculation was done only once
    with caplog.at_level('DEBUG'):
        assert MyClass.expensive_calculation == 499500
        assert 'Calculating...' in caplog.text
        
        # Second access should not trigger a new calculation due to caching
        assert MyClass.expensive_calculation == 499500

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_edge_case.py:5:0: E0102: function already defined line 3 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_edge_case.py:23:8: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)


"""