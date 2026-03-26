
from dataclasses import is_dataclass
from typing import Optional, Type, Callable, Union
from dataclasses_json.api import _process_class
from dataclasses_json.enums import LetterCase, Undefined

def dataclass_json(_cls: Optional[Type[T]] = None, *, letter_case: Optional[LetterCase] = None,
                   undefined: Optional[Union[str, Undefined]] = None) -> Union[Callable[[Type[T]], Type[T]], Type[T]]:
    """
    A decorator that simplifies the integration of dataclasses with JSON handling. It allows for customization of letter case and handling of undefined values when converting between Python objects and JSON.

    Parameters:
        _cls (Optional[Type[T]]): The dataclass to be decorated. If not provided, the decorator returns a function that can be used to decorate a class.
        letter_case (Optional[LetterCase]): Specifies the desired letter case for the JSON keys. Accepted values are from the `LetterCase` enum:
            - `LetterCase.CAMEL`: Converts field names to camelCase.
            - `LetterCase.SNAKE`: Converts field names to snake_case.
            - `LetterCase.PASCAL`: Converts field names to PascalCase.
            - `LetterCase.NONE`: Leaves the field names as they are in the dataclass (default).
        undefined (Optional[Union[str, Undefined]]): Specifies how to handle undefined values during JSON serialization. Accepted values:
            - A string representing a placeholder value for undefined fields (e.g., 'undefined').
            - The `Undefined` enum from this module, which can be used to exclude undefined fields entirely.

    Returns:
        Union[Callable[[Type[T]], Type[T]], Type[T]]: If _cls is provided, returns the decorated dataclass; otherwise, returns a decorator function that can be applied to other dataclasses.

    Example:
        @dataclass_json
        @dataclass_json(letter_case=LetterCase.CAMEL)
        class Example:
            # Fields here...
            pass

        This will decorate the `Example` class, converting its fields to camelCase in JSON representations and handling undefined values according to the specified method.
    """

    def wrap(cls: Type[T]) -> Type[T]:
        return _process_class(cls, letter_case, undefined)

    if _cls is None:
        return wrap
    return wrap(_cls)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:5:0: E0401: Unable to import 'dataclasses_json.enums' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:5:0: E0611: No name 'enums' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:7:39: E0602: Undefined variable 'T' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:8:94: E0602: Undefined variable 'T' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:8:104: E0602: Undefined variable 'T' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:8:114: E0602: Undefined variable 'T' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:36:23: E0602: Undefined variable 'T' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_edge_cases.py:36:35: E0602: Undefined variable 'T' (undefined-variable)

"""