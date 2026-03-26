
import unittest
from pytutils.ext.rwclassproperty import classproperty
from unittest.mock import patch, sentinel

class TestClassProperty(unittest.TestCase):
    def test_read_only(self):
        class Z(object, metaclass=classproperty.meta):
            _get_set = sentinel.nothing

            @classproperty
            def get_only(cls):
                return sentinel.get_only

        self.assertEqual(sentinel.get_only, Z.get_only)
        with self.assertRaises(AttributeError):
            Z.get_only = 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_valid_input.py:12:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""