
import pytest
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

# Define a CatchAllVar type as Optional[Dict]
CatchAllVar = Optional[Dict[str, Any]]

@dataclass
class Example(_CatchAllUndefinedParameters):
    defined_param: int
    catch_all: CatchAllVar = field(default_factory=dict)




def test_handle_dump_none_catch_all():
    example_instance = Example(defined_param=10, catch_all=None)
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(example_instance)

def test_handle_dump_invalid_inputs():
    invalid_instance_no_catch_all = Example(defined_param=10)
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(invalid_instance_no_catch_all)