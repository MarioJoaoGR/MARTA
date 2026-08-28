
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








def test_myclass_with_no_positional_arguments_and_unknown_fields():
    with pytest.raises(TypeError):
        # This will raise an error if `defined_field` is required and not provided
        MyClass(key1='value1', key2='value2')