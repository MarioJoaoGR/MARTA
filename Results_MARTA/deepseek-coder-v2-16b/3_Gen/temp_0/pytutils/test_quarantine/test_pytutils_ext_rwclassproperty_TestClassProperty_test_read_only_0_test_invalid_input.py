
import unittest
from pytutils.ext.rwclassproperty import classproperty

class TestClassProperty(unittest.TestCase):

    def test_read_only(self):
        """
        This function demonstrates the creation of a class property that is read-only.
        
        It defines a class `Z` with a class property `get_only` using the `classproperty` decorator from the `pytutils.ext.rwclassproperty` module. The `get_only` property can be accessed like a class attribute but cannot be set once defined, raising an AttributeError if attempted.
        
        Parameters:
            None
            
        Returns:
            None
            
        Example Usage:
            This function does not take any parameters and does not return anything. It is intended to be run as part of a test suite where it demonstrates the behavior of read-only class properties.
        """
        sentinel = object()  # Assuming sentinel is defined somewhere in your module or globally
        
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
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_invalid_input.py:25:23: E1101: Instance of 'object' has no 'nothing' member (no-member)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_invalid_input.py:28:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_invalid_input.py:29:23: E1101: Instance of 'object' has no 'get_only' member (no-member)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_invalid_input.py:31:25: E1101: Instance of 'object' has no 'get_only' member (no-member)


"""