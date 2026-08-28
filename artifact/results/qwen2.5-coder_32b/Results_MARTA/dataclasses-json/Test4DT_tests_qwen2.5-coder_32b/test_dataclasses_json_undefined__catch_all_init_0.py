
import pytest
from dataclasses import dataclass, field
from typing import Optional, Dict
from dataclasses_json.undefined import _CatchAllUndefinedParameters

# Assuming CatchAllVar is defined as Optional[Dict]
CatchAllVar = Optional[Dict]

@dataclass
class MyClass(_CatchAllUndefinedParameters):
    defined_field: int
    catch_all: CatchAllVar = field(default_factory=dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._catch_all_init(*args, **kwargs)

def _catch_all_init(self, *args, **kwargs):
    known_kwargs, unknown_kwargs = \
        _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
            self, kwargs)
    num_params_takeable = len(
        self.__class__.__init__.__signature__.parameters) - 1  # don't count self
    if _CatchAllUndefinedParameters._get_catch_all_field(
            self).name not in known_kwargs:
        num_params_takeable -= 1
    num_args_takeable = num_params_takeable - len(known_kwargs)

    args, unknown_args = args[:num_args_takeable], args[num_args_takeable:]
    bound_parameters = self.__class__.__init__.__signature__.bind_partial(self, *args, **known_kwargs)

    unknown_args = {f"_UNKNOWN{i}": v for i, v in enumerate(unknown_args)}
    arguments = bound_parameters.arguments
    arguments.update(unknown_args)
    arguments.update(unknown_kwargs)
    arguments.pop("self", None)
    final_parameters = _CatchAllUndefinedParameters.handle_from_dict(
        self, arguments)
    original_init(self, **final_parameters)

# Patching the _catch_all_init method to use our custom implementation
MyClass._catch_all_init = _catch_all_init




def test_myclass_with_no_positional_arguments_and_unknown_fields():
    with pytest.raises(TypeError):
        # This should raise a TypeError because defined_field is required and not provided
        obj = MyClass(key1='value1', key2='value2')