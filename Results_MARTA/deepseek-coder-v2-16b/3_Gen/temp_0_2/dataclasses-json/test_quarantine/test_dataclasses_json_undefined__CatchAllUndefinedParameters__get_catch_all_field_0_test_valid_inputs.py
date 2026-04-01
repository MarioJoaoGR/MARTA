
import sys
from dataclasses import fields, get_type_hints
from typing import Optional
from dataclasses_json.undefined import UndefinedParameterError
from dataclasses_json import CatchAllVar

class _CatchAllUndefinedParameters:
    """
        This class allows to add a field of type utils.CatchAll which acts as a
        dictionary into which all undefined parameters will be written. These
        parameters are not affected by LetterCase. If no undefined parameters are given,
        this dictionary will be empty.
        
        Attributes:
            cls (class): The class for which to retrieve the catch-all field.
            
        Returns:
            Field: The single catch-all field of the specified class.
            
        Raises:
            UndefinedParameterError: If no field of type dataclasses_json.CatchAll is defined or if multiple catch-all fields are supplied.
            
        Examples:
            To use this method, you would typically call it on a class instance where a CatchAll field has been defined:
            
            ```python
            class MyClass:
                my_field: utils.CatchAll = None
            
            catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(MyClass)
            print(catch_all_field)  # Output will be the field object of type utils.CatchAll in MyClass
            ```
    """
    class _SentinelNoDefault:
        pass
    
    @staticmethod
    def _get_catch_all_field(cls):
        cls_globals = vars(sys.modules[cls.__module__])
        types = get_type_hints(cls, globalns=cls_globals)
        catch_all_fields = list(
            filter(lambda f: types[f.name] == Optional[CatchAllVar], fields(cls)))
        number_of_catch_all_fields = len(catch_all_fields)
        if number_of_catch_all_fields == 0:
            raise UndefinedParameterError(
                "No field of type dataclasses_json.CatchAll defined")
        elif number_of_catch_all_fields > 1:
            raise UndefinedParameterError(
                f"Multiple catch-all fields supplied: "
                f"{number_of_catch_all_fields}.")
        else:
            return catch_all_fields[0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_valid_inputs.py:3:0: E0611: No name 'get_type_hints' in module 'dataclasses' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters__get_catch_all_field_0_test_valid_inputs.py:6:0: E0611: No name 'CatchAllVar' in module 'dataclasses_json' (no-name-in-module)


"""