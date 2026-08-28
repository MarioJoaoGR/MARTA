
import pytest
from dataclasses import dataclass, fields, Field
from typing import Optional, Dict
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

# Define CatchAllVar as an alias for Optional[Dict]
CatchAllVar = Optional[Dict]

@dataclass
class Example(_CatchAllUndefinedParameters):
    defined_param: int
    catch_all: CatchAllVar = None


def test_get_catch_all_field_no_catch_all_field():
    """Test that _get_catch_all_field raises an error if no catch-all field is defined."""
    @dataclass
    class NoCatchAllField(_CatchAllUndefinedParameters):
        defined_param: int

    with pytest.raises(UndefinedParameterError) as excinfo:
        NoCatchAllField._get_catch_all_field(NoCatchAllField)
    assert str(excinfo.value) == "No field of type dataclasses_json.CatchAll defined"
