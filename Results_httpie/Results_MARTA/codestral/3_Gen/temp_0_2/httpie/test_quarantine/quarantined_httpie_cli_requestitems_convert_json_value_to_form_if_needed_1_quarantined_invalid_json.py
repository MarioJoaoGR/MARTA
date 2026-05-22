
import functools
from typing import Callable, Union
from httpie.cli.requestitems import KeyValueArg, JSONType
from httpie.plugins.errors import ParseError

def convert_json_value_to_form_if_needed(in_json_mode: bool, processor: Callable[[KeyValueArg], JSONType]) -> Callable[[], str]:
    """
    Converts a JSON value to a form if needed.

    This function checks whether the input is in JSON mode and processes it accordingly. If in JSON mode, it directly returns the processor function. Otherwise, it wraps the processor function with additional logic to handle complex JSON values by converting them to strings or raising an error if they cannot be serialized for form submission.

    Parameters:
        in_json_mode (bool): A boolean flag indicating whether the input is in JSON mode.
        processor (Callable[[KeyValueArg], JSONType]): The processing function that takes KeyValueArg and returns a JSON type.

    Returns:
        Callable[[], str]: A callable function that, when invoked, processes the data and returns it as a string.

    Raises:
        ParseError: If the processor output is not a primitive type (str, int, float) and cannot be serialized for form submission.
    """
    if in_json_mode:
        return processor

    @functools.wraps(processor)
    def wrapper(*args, **kwargs) -> str:
        try:
            output = processor(*args, **kwargs)
        except ParseError:
            output = None
        if isinstance(output, (str, int, float)):
            return str(output)
        else:
            raise ParseError('Cannot use complex JSON value types with --form/--multipart.')

    return wrapper

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_requestitems_convert_json_value_to_form_if_needed_1_test_invalid_json
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_convert_json_value_to_form_if_needed_1_test_invalid_json.py:5:0: E0401: Unable to import 'httpie.plugins.errors' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_convert_json_value_to_form_if_needed_1_test_invalid_json.py:5:0: E0611: No name 'errors' in module 'httpie.plugins' (no-name-in-module)


"""