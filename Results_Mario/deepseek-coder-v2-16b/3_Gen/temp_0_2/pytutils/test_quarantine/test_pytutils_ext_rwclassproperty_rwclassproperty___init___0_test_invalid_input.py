
from pytutils.ext.rwclassproperty import rwclassproperty
import unittest

class TestInvalidInput(unittest.TestCase):
    def test_invalid_setter_prop(self):
        class InvalidSetterClass:
            @rwclassproperty
            def invalid_setter_prop(cls, value):  # Corrected method signature to include 'self'
                pass
        
        with self.assertRaises(AttributeError):
            InvalidSetterClass.invalid_setter_prop = 123  # This should raise an error because the property does not accept arguments in its setter

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0_test_invalid_input.py:9:12: E0213: Method 'invalid_setter_prop' should have "self" as first argument (no-self-argument)


"""