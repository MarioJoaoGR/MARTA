
# Module: pytutils.ext.rwclassproperty
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

# Example 1: Simple Read-Write Property
class Z(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def foo(cls):
        return 123
    
    _bar = None
    
    @rwclassproperty
    def bar(cls):
        return cls._bar
    
    @bar.setter
    def bar(cls, value):
        cls._bar = value

def test_simple_read_write_property():
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

# Example 2: Read-Only Property
class ZReadOnly(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def foo(cls):
        return 123

def test_read_only_property():
    assert ZReadOnly.foo == 123
    with pytest.raises(AttributeError):
        ZReadOnly.foo = 456

# Example 3: Using Setter Method
class ZSetter(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def baz(cls):
        return cls._baz
    
    @baz.setter
    def baz(cls, value):
        cls._baz = value

def test_using_setter_method():
    assert ZSetter.baz is None
    ZSetter.baz = 333
    assert ZSetter.baz == 333

# Example 4: Chaining Setter Method
class ZChaining(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def qux(cls):
        return cls._qux
    
    @qux.setter
    def qux(cls, value):
        cls._qux = value

def test_chaining_setter_method():
    assert ZChaining.qux is None
    ZChaining.qux = 444
    assert ZChaining.qux == 444

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:31:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:42:4: E0213: Method 'baz' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:46:4: E0213: Method 'baz' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:57:4: E0213: Method 'qux' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:61:4: E0213: Method 'qux' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:7:0: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:29:0: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:40:0: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0.py:55:0: E0602: Undefined variable 'ClassPropertyMeta' (undefined-variable)


"""