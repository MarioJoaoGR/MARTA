
import functools
from typing import Callable, Union
from httpie.cli.requestitems import ParseError

JSONType = Union[str, int, float, list, dict, None]
KeyValueArg = dict  # Assuming KeyValueArg is a dictionary for simplicity

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
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
============================ no tests ran in 0.25s =============================
"""