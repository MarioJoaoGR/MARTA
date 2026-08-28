
import pytest
from dataclasses import dataclass, field
from dataclasses_json.undefined import _CatchAllUndefinedParameters, Field

# Assuming CatchAll is defined as a type alias for Dict[str, Any]
CatchAll = dict

@dataclass
class MyDataClass:
    defined_field: int
    catch_all_field: CatchAll = field(default_factory=dict)


def test_get_default_with_no_default_or_factory():
    catch_all_field = field(default_factory=dict)
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == {}

def test_get_default_with_default_value():
    catch_all_field = field(default={'initial': 'value'})
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == {'initial': 'value'}

def test_get_default_with_default_factory():
    catch_all_field = field(default_factory=lambda: {'factory': 'value'})
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == {'factory': 'value'}