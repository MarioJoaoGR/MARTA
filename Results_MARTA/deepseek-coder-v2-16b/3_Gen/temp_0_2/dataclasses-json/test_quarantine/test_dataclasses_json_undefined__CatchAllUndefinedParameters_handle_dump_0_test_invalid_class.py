
from dataclasses import dataclass
from typing import Any, Dict
import pytest
from dataclasses_json.undefined import UndefinedType

@dataclass
class _CatchAllUndefinedParameters:
    """
        This class allows to add a field of type utils.CatchAll which acts as a
        dictionary into which all
        undefined parameters will be written.
        These parameters are not affected by LetterCase.
        If no undefined parameters are given, this dictionary will be empty.
    """
    class _SentinelNoDefault:
        pass

def handle_dump(obj) -> Dict[Any, Any]:
    """
    Retrieves the single catch-all field from a specified class, if it exists. The catch-all field is used to collect all undefined parameters that are not otherwise defined by other fields in the class. This method is particularly useful for handling configuration settings where any unspecified parameters should be captured and stored.
    
    Parameters:
        cls (class): The class for which to retrieve the catch-all field. It must be a class object that has been decorated with a utils.CatchAll field.
        
    Returns:
        Field: The single catch-all field of the specified class, or None if no such field is found.
        
    Raises:
        UndefinedParameterError: If no field of type dataclasses_json.CatchAll is defined for the class, or if multiple catch-all fields are present in the class definition.
        
    Examples:
        To use this method to retrieve a catch-all field from a class named `MyClass` that has been decorated with utils.CatchAll:
        
        ```python
        class MyClass:
            my_field: utils.CatchAll = None
        
        catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(MyClass)
        print(catch_all_field)  # Output will be the field object of type utils.CatchAll in MyClass
        ```
    """
    catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(cls=obj.__class__)
    return getattr(obj, catch_all_field.name) if catch_all_field else {}

# Test case to check the handle_dump function with an invalid class
@pytest.mark.parametrize("invalid_class", [int, str])
def test_handle_dump_with_invalid_class(invalid_class):
    """
    This test checks that handle_dump raises a UndefinedParameterError when passed an instance of an invalid class type.
    """
    with pytest.raises(UndefinedType):
        handle_dump(invalid_class())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_class
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_class.py:5:0: E0611: No name 'UndefinedType' in module 'dataclasses_json.undefined' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_invalid_class.py:43:22: E1101: Class '_CatchAllUndefinedParameters' has no '_get_catch_all_field' member (no-member)


"""