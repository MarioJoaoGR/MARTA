
from pytutils.props import roclassproperty
import unittest

class TestRoClassProperty(unittest.TestCase):
    def setUp(self):
        class MyClass:
            @roclassproperty
            def my_prop(cls):
                return "This is a read-only property"
        
        self.obj = MyClass()
        self.my_class = MyClass

    def test_read_only_property(self):
        # Test accessing the property
        self.assertEqual("This is a read-only property", self.obj.my_prop)
        
        with self.assertRaises(AttributeError):
            # Attempt to set the property, which should raise an AttributeError
            self.obj.my_prop = "Attempt to modify the property"

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_edge_case
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_edge_case.py:9:12: E0213: Method 'my_prop' should have "self" as first argument (no-self-argument)


"""