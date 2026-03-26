
from dataclasses import dataclass
from dataclasses_json import CatchAllVar, UndefinedParameterError
import sys
from typing import Optional, Dict, Any

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
    
    @staticmethod
    def handle_dump(obj) -> Dict[Any, Any]:
        """
        Retrieves the single catch-all field of a specified class, which is used to capture all undefined parameters. This method is part of the `_CatchAllUndefinedParameters` class and is designed to handle the retrieval of such fields across different classes.
        
        Parameters:
            obj (object): The object for which to get the catch-all field. It must be an instance with at least one field annotated with `utils.CatchAll`.
            
        Returns:
            Dict[Any, Any]: The dictionary containing all undefined parameters captured by the catch-all field.
        
        Raises:
            UndefinedParameterError: If no field of type `utils.CatchAll` is defined in the class or if more than one catch-all field is present.
        
        Example:
            To use this function, you would call it on a class instance where you want to capture all undefined parameters. For example:
            
            ```python
            from dataclasses import dataclass
            from dataclasses_json import CatchAllVar, UndefinedParameterError
            import sys
            from typing import Optional

            @dataclass
            class ExampleClass:
                field1: str
                field2: int
                # Assuming this is the only catch-all field in the class
                utils.CatchAll = None

            catch_all_dict = _CatchAllUndefinedParameters.handle_dump(ExampleClass)
            ```
        """
        catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(obj)
        return getattr(obj, catch_all_field.name)
    
    @staticmethod
    def _get_catch_all_field(cls):
        catch_all_fields = [
            field for name, field in cls.__dataclass_fields__.items() 
            if isinstance(field.metadata.get('dataclasses_json', {}).get('encoder'), CatchAllVar)
        ]
        
        if len(catch_all_fields) != 1:
            raise UndefinedParameterError("Expected exactly one catch-all field, but found {}".format(len(catch_all_fields)))
        
        return catch_all_fields[0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_error_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_error_case.py:3:0: E0611: No name 'CatchAllVar' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_handle_dump_0_test_error_case.py:3:0: E0611: No name 'UndefinedParameterError' in module 'dataclasses_json' (no-name-in-module)

"""