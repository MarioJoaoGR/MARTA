
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

@dataclass
class NoCatchAllField(_CatchAllUndefinedParameters):
    defined_param: int

@dataclass
class ExampleMultipleCatchAll(_CatchAllUndefinedParameters):
    defined_param: int
    catch_all1: CatchAllVar = None
    catch_all2: CatchAllVar = None


def test_no_catch_all_field():
    with pytest.raises(UndefinedParameterError) as excinfo:
        NoCatchAllField._get_catch_all_field(NoCatchAllField)
    assert str(excinfo.value) == "No field of type dataclasses_json.CatchAll defined"

