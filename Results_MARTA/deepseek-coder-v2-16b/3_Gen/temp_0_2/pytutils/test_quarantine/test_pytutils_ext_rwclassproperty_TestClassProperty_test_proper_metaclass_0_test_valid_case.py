
import pytest
from pytutils.ext.rwclassproperty import classproperty
from pytutils.ext.rwclassproperty import sentinel

class TestClassProperty:

    def test_proper_metaclass(self):
        class Z(object):
            _get_set = sentinel.nothing

            @classproperty
            def get_only(cls):
                return cls._get_set

        with pytest.raises(TypeError):
            # Attempting to access get_only as an instance attribute should raise a TypeError
            Z.get_only

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_case.py:13:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""