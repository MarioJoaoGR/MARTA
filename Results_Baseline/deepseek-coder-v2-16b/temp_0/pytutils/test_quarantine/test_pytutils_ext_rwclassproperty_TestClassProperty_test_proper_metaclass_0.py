
from unittest import TestCase
from pytutils.ext.rwclassproperty import TestClassProperty
from pytutils.ext.rwclassproperty import sentinel  # Assuming sentinel is defined elsewhere

class TestZ(TestCase):
    def test_proper_metaclass(self):
        class Z(object):
            _get_set = sentinel.nothing

            @TestClassProperty
            def get_only(cls):
                return sentinel.get_only

        with self.assertRaises(TypeError):
            self.assertEqual("should not resolve", Z.get_only)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0.py:12:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""