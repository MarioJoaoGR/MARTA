
import unittest
from pytutils.ext.rwclassproperty import classproperty
from tests.mocks import sentinel

class TestClassProperty(unittest.TestCase):
    def test_proper_metaclass(self):
        class Z(object):
            _get_set = sentinel.nothing

            @classproperty
            def get_only(cls):
                return sentinel.get_only

        with self.assertRaises(TypeError):
            self.assertEqual("should not resolve", Z.get_only)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_input.py:4:0: E0401: Unable to import 'tests.mocks' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_input.py:4:0: E0611: No name 'mocks' in module 'tests' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_proper_metaclass_0_test_valid_input.py:12:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""