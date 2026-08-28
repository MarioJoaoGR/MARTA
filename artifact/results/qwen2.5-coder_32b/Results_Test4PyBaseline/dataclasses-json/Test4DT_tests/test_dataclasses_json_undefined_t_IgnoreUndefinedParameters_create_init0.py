
# Test case  
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _IgnoreUndefinedParameters

class TestCreateInit:
    def test_ignore_undefined_parameters(self):
        @dataclass
        class MyClass(_IgnoreUndefinedParameters):
            a: int
            b: int

        MyClass.__init__ = _IgnoreUndefinedParameters.create_init(MyClass)
        obj = MyClass(a=1, b=2, c=3)  # 'c' is ignored as it's not defined in the original __init__
        assert obj.a == 1
        assert obj.b == 2

    def test_no_extra_parameters(self):
        @dataclass
        class AnotherClass(_IgnoreUndefinedParameters):
            x: int
            y: int
            z: int = None

        AnotherClass.__init__ = _IgnoreUndefinedParameters.create_init(AnotherClass)
        obj = AnotherClass(x=10, y=20)  # No extra parameters
        assert obj.x == 10
        assert obj.y == 20
        assert obj.z is None

    def test_all_extra_parameters(self):
        @dataclass
        class YetAnotherClass(_IgnoreUndefinedParameters):
            p: int
            q: int

        YetAnotherClass.__init__ = _IgnoreUndefinedParameters.create_init(YetAnotherClass)
        obj = YetAnotherClass(p=100, q=200, r=300, s=400)  # All extra parameters are ignored
        assert obj.p == 100
        assert obj.q == 200

    def test_no_parameters(self):
        @dataclass
        class NoParamClass(_IgnoreUndefinedParameters):
            pass

        NoParamClass.__init__ = _IgnoreUndefinedParameters.create_init(NoParamClass)
        obj = NoParamClass(a=1, b=2)  # All parameters are ignored
        assert True  # Just ensuring no error is raised and object is created

    def test_default_values(self):
        @dataclass
        class DefaultValuesClass(_IgnoreUndefinedParameters):
            a: int
            b: int = 5

        DefaultValuesClass.__init__ = _IgnoreUndefinedParameters.create_init(DefaultValuesClass)
        obj = DefaultValuesClass(a=10)  # Using default value for 'b'
        assert obj.a == 10
        assert obj.b == 5

    def test_positional_arguments(self):
        @dataclass
        class PositionalArgsClass(_IgnoreUndefinedParameters):
            a: int
            b: int

        PositionalArgsClass.__init__ = _IgnoreUndefinedParameters.create_init(PositionalArgsClass)
        obj = PositionalArgsClass(10, 20, c=30)  # 'c' is ignored as it's not defined in the original __init__
        assert obj.a == 10
        assert obj.b == 20

    def test_mixed_positional_and_keyword_arguments(self):
        @dataclass
        class MixedArgsClass(_IgnoreUndefinedParameters):
            a: int
            b: int
            c: int = 30

        MixedArgsClass.__init__ = _IgnoreUndefinedParameters.create_init(MixedArgsClass)
        obj = MixedArgsClass(10, b=20, d=40)  # 'd' is ignored as it's not defined in the original __init__
        assert obj.a == 10
        assert obj.b == 20