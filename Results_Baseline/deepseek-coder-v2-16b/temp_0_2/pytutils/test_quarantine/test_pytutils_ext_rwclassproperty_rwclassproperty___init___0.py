
# Module: pytutils.ext.rwclassproperty
import pytest
from classproperty import ClassPropertyMeta, classproperty

# Define a test class with ClassPropertyMeta as its metaclass
class TestClass:
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

# Test cases for read-write class property
def test_read_write_class_property():
    assert TestClass.foo == 123
    assert TestClass.bar is None
    TestClass.bar = 222
    assert TestClass.bar == 222

# Test cases for read-only class property
def test_read_only_class_property():
    class ReadOnlyTestClass(object, metaclass=ClassPropertyMeta):
        @classproperty
        def foo(cls):
            return 123

    assert ReadOnlyTestClass.foo == 123
    with pytest.raises(AttributeError):
        ReadOnlyTestClass.foo = 456

# Test cases for custom metaclass usage
def test_custom_metaclass():
    class MyMeta(ClassPropertyMeta):
        pass

    class CustomMetaclassTestClass(object, metaclass=MyMeta):
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

    assert CustomMetaclassTestClass.foo == 123
    assert CustomMetaclassTestClass.bar is None
    CustomMetaclassTestClass.bar = 222
    assert CustomMetaclassTestClass.bar == 222

# Test cases for factory function usage
def test_factory_function():
    def get_foo(cls):
        return 123

    def set_foo(cls, value):
        pass

    class FactoryFunctionTestClass:
        foo = rwclassproperty(get_foo, set_foo)

    assert FactoryFunctionTestClass.foo == 123
    with pytest.raises(AttributeError):
        FactoryFunctionTestClass.foo = 456

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___init___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:33:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:42:17: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:45:4: E1139: Invalid metaclass 'MyMeta' used (invalid-metaclass)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:47:8: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:53:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:57:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:74:14: E0602: Undefined variable 'rwclassproperty' (undefined-variable)


"""