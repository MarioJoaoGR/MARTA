
# Module: dataclasses_json.undefined
import pytest
from dataclasses import dataclass, field
from typing import Optional, Dict
from dataclasses_json.undefined import _CatchAllUndefinedParameters, CatchAllVar, UndefinedParameterError

# Example dataclass using the _CatchAllUndefinedParameters
@dataclass
class ExampleDataClass(_CatchAllUndefinedParameters):
    defined_field: int
    catch_all: Optional[CatchAllVar] = field(default_factory=dict)

def test_catch_all_with_defined_and_undefined_fields():
    # Correctly pass undefined fields as a dictionary to the catch_all parameter
    instance = ExampleDataClass(defined_field=10, catch_all={'undefined_field': 'value'})
    assert instance.defined_field == 10
    assert instance.catch_all == {'undefined_field': 'value'}

def test_catch_all_with_multiple_undefined_fields():
    # Correctly pass undefined fields as a dictionary to the catch_all parameter
    instance = ExampleDataClass(
        defined_field=10,
        catch_all={'extra_param1': 'extra_value1', 'extra_param2': 'extra_value2'}
    )
    assert instance.defined_field == 10
    assert instance.catch_all == {'extra_param1': 'extra_value1', 'extra_param2': 'extra_value2'}

def test_catch_all_with_no_undefined_fields():
    instance = ExampleDataClass(defined_field=10)
    assert instance.defined_field == 10
    assert instance.catch_all == {}

def test_get_catch_all_field_single_field():
    # Correctly call the static method with the class itself as an argument
    catch_all_field = ExampleDataClass._get_catch_all_field(ExampleDataClass)
    assert catch_all_field.name == 'catch_all'
    assert catch_all_field.type == Optional[CatchAllVar]

def test_get_catch_all_field_no_catch_all_field():
    @dataclass
    class NoCatchAllField(_CatchAllUndefinedParameters):
        defined_field: int

    # Correctly call the static method with the class itself as an argument
    with pytest.raises(UndefinedParameterError, match="No field of type dataclasses_json.CatchAll defined"):
        NoCatchAllField._get_catch_all_field(NoCatchAllField)

def test_get_catch_all_field_multiple_catch_all_fields():
    @dataclass
    class MultipleCatchAllFields(_CatchAllUndefinedParameters):
        defined_field: int
        catch_all1: Optional[CatchAllVar] = field(default_factory=dict)
        catch_all2: Optional[CatchAllVar] = field(default_factory=dict)

    # Correctly call the static method with the class itself as an argument
    with pytest.raises(UndefinedParameterError, match="Multiple catch-all fields supplied: 2."):
        MultipleCatchAllFields._get_catch_all_field(MultipleCatchAllFields)
