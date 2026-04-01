
from pytutils.props import lazyperclassproperty
import unittest

class MyClass1:
    pass

class MyClass2(MyClass1):
    pass

def expensive_calculation(cls):
    return cls()

class TestLazyPerClassProperty(unittest.TestCase):
    
    def test_valid_case(self):
        @lazyperclassproperty(expensive_calculation)
        def cached_instance(cls):
            pass
        
        # First access will trigger the expensive calculation
        self.assertIsInstance(MyClass1.cached_instance, MyClass1)
        self.assertIsInstance(MyClass2.cached_instance, MyClass2)
        
        # Subsequent accesses for the same class will return the cached result
        self.assertIsInstance(MyClass1.cached_instance, MyClass1)
        self.assertIsInstance(MyClass2.cached_instance, MyClass2)

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:22:30: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:23:30: E1101: Class 'MyClass2' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:26:30: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:27:30: E1101: Class 'MyClass2' has no 'cached_instance' member (no-member)


"""