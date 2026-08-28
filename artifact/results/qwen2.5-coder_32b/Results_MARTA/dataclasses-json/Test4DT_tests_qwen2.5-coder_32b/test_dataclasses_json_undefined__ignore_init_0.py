
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _IgnoreUndefinedParameters
import inspect
import functools

# Define the dataclass MyClass
@dataclass
class MyClass:
    param1: str
    param2: int

# Modify the __init__ method to ignore undefined parameters
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

MyClass.__init__ = create_init(MyClass)

# Test cases
def test_happy_path():
    obj = MyClass(param1='value1', param2=42, extra_param='ignored')
    assert obj.param1 == 'value1'
    assert obj.param2 == 42

def test_edge_cases():
    obj = MyClass(param1=None, param2=0)
    assert obj.param1 is None
    assert obj.param2 == 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        MyClass()
