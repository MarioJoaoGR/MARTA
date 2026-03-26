
# Module: pytutils.ext.rwclassproperty
import pytest
from classproperty import ClassPropertyMeta, classproperty

# Example usage of defining a class with a read-write property
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

# Test cases for the read-write class property
def test_read_write_property():
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

# Example usage of defining a class with a read-only property
class ReadOnlyClass(metaclass=ClassPropertyMeta):
    @classproperty
    def ro_prop(cls):
        return "Read-Only Value"

# Test cases for the read-only class property
def test_read_only_property():
    with pytest.raises(AttributeError) as excinfo:
        ReadOnlyClass.ro_prop = "Try to Set This"
    assert str(excinfo.value) == "can't set attribute"
    assert ReadOnlyClass.ro_prop == "Read-Only Value"

# Example usage of defining a class with both read-write and read-only properties
class MixedPropertiesClass(metaclass=ClassPropertyMeta):
    @classproperty
    def rw_prop(cls):
        return 456

    @rw_prop.setter
    def rw_prop(cls, value):
        pass  # Placeholder for setting the property

    @classproperty
    def ro_prop(cls):
        return "Read-Only Value"

# Test cases for mixed properties
def test_mixed_properties():
    assert MixedPropertiesClass.rw_prop == 456
    with pytest.raises(AttributeError) as excinfo:
        MixedPropertiesClass.ro_prop = "Try to Set This"
    assert str(excinfo.value) == "can't set attribute"
    assert MixedPropertiesClass.ro_prop == "Read-Only Value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___set___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:32:4: E0213: Method 'ro_prop' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:45:4: E0213: Method 'rw_prop' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:49:4: E0213: Method 'rw_prop' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___set___0.py:53:4: E0213: Method 'ro_prop' should have "self" as first argument (no-self-argument)


"""