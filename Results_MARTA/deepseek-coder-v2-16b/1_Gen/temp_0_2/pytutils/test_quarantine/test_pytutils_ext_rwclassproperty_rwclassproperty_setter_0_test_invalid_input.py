
import pytest
from pytutils.ext import rwclassproperty

def test_invalid_input():
    with pytest.raises(TypeError):
        class InvalidClass:
            @rwclassproperty.setter
            def foo(cls, value):
                pass

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_invalid_input.py:9:12: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_invalid_input.py:8:13: E1101: Module 'pytutils.ext.rwclassproperty' has no 'setter' member (no-member)


"""