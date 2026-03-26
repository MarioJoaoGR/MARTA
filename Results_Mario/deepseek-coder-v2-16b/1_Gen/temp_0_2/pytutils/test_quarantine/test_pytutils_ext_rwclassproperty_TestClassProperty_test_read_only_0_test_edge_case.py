
import unittest
from pytutils.ext.rwclassproperty import classproperty

class TestClassProperty(unittest.TestCase):
    def test_read_only(self):
        """
        A function that tests the read-only property of a class defined using the `classproperty` decorator from the `pytutils.ext.rwclassproperty` module.
        
        The function defines a subclass `Z` of `object` with a metaclass that includes the `classproperty` decorator. The `get_only` attribute is defined to be read-only, and its value can only be retrieved but not set. The test checks if attempting to set the `get_only` attribute raises an `AttributeError`.
        
        Parameters:
            None
            
        Returns:
            None
            
        Example Usage:
            The example provided in the source code will raise an AttributeError when attempting to assign a value to `Z.get_only`, 
            demonstrating that this attribute is read-only.
        
        """
        class Z(object, metaclass=classproperty.meta):
            _get_set = object()

            @classproperty
            def get_only(cls):
                return cls._get_set

        self.assertEqual(Z._get_set, Z.get_only)
        with self.assertRaises(AttributeError):
            Z.get_only = 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_TestClassProperty_test_read_only_0_test_edge_case.py:27:12: E0213: Method 'get_only' should have "self" as first argument (no-self-argument)


"""