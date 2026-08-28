
import pytest
from dataclasses import dataclass, fields
import inspect
import functools
from dataclasses_json.undefined import _CatchAllUndefinedParameters

class _IgnoreUndefinedParameters:
    @staticmethod
    def handle_from_dict(cls, kvs):
        known_given_parameters, _ = \
            _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                cls=cls, kvs=kvs)
        return known_given_parameters

    @staticmethod
    def create_init(obj):
        original_init = obj.__init__
        init_signature = inspect.signature(original_init)

        @functools.wraps(obj.__init__)
        def _ignore_init(self, *args, **kwargs):
            known_kwargs, _ = \
                _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                    obj, kwargs)
            num_params_takeable = len(
                init_signature.parameters) - 1  # don't count self
            num_args_takeable = num_params_takeable - len(known_kwargs)

            args = args[:num_args_takeable]
            bound_parameters = init_signature.bind_partial(self, *args,
                                                           **known_kwargs)
            bound_parameters.apply_defaults()

            arguments = bound_parameters.arguments
            arguments.pop("self", None)
            final_parameters = \
                _IgnoreUndefinedParameters.handle_from_dict(obj, arguments)
            original_init(self, **final_parameters)

        return _ignore_init

@dataclass
class MyClass:
    param1: str
    param2: int

# Modify the __init__ method to ignore undefined parameters
MyClass.__init__ = _IgnoreUndefinedParameters.create_init(MyClass)

def test_valid_initialization():
    obj = MyClass(param1='value1', param2=42)
    assert obj.param1 == 'value1'
    assert obj.param2 == 42

def test_extra_parameters_ignored():
    obj = MyClass(param1='value1', param2=42, extra_param='ignored')
    assert obj.param1 == 'value1'
    assert obj.param2 == 42

def test_missing_required_parameter_raises_TypeError():
    with pytest.raises(TypeError):
        MyClass(param1='value1')


