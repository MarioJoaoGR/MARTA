
# Module: pytutils.ext.rwclassproperty
# Import the function properly using the provided module name.
from pytutils.ext.rwclassproperty import rwclassproperty, ClassPropertyMeta, classproperty

import pytest

# Test cases for defining a class with read-write class property
def test_read_write_class_property():
    # Define a class using the custom metaclass
    class Z(object, metaclass=ClassPropertyMeta):
        @classproperty
        def foo(cls):
            return 123

        _bar = None

        @classproperty
        def bar(cls):
            return cls._bar

        @bar.setter
        def bar(cls, value):
            cls._bar = value

    # Accessing class properties
    assert Z.foo == 123
    assert Z.bar is None

    # Setting the property
    Z.bar = 222
    assert Z.bar == 222

# Test cases for creating an instance of rwclassproperty with only a getter
def test_rwclassproperty_getter():
    @classproperty
    def foo(cls):
        return 123

    # Usage
    class Z(object, metaclass=ClassPropertyMeta):
        prop = rwclassproperty(foo)

    assert Z.prop == 123

# Test cases for creating an instance of rwclassproperty with both getter and setter
def test_rwclassproperty_getter_setter():
    @classproperty
    def foo(cls):
        return 123

    @foo.setter
    def foo(cls, value):
        pass  # Placeholder for setter logic

    # Usage
    class Z(object, metaclass=ClassPropertyMeta):
        prop = rwclassproperty(foo, foo.setter)

    assert Z.prop == 123
    Z.prop = 456  # This will call the setter function (placeholder logic)
    assert Z.prop == 456

# Run all test cases
if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:13:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:19:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:23:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""