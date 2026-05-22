
import json
from httpie.cli.requestitems import KeyValueArg, ParseError
from unittest.mock import patch

def load_json(arg: KeyValueArg, contents: str) -> JSONType:
    """
    Loads a JSON string while preserving the order of key-value pairs and allowing duplicate keys.

    This function takes a JSON string as input, parses it with a custom object_pairs_hook to ensure that the resulting dictionary preserves both the insertion order of key-value pairs and allows for duplicate keys using a custom class `JsonDictPreservingDuplicateKeys`. If the parsing fails due to an invalid JSON format or other issues, it raises a `ParseError` with a detailed error message indicating the origin of the input.

    Parameters:
        arg (KeyValueArg): An object containing information about the key-value pair being parsed. Specifically, its `orig` attribute is used to provide context for any errors that occur during parsing.
        contents (str): The JSON string to be parsed. This should be a valid JSON formatted string.

    Returns:
        dict: A dictionary with preserved order and duplicate keys support.

    Raises:
        ParseError: If the input string is not a valid JSON format or if there are issues during parsing, this exception is raised with an error message indicating the origin of the input.

    Example:
        >>> import json
        >>> from httpie.cli.requestitems import load_json
        >>> arg = KeyValueArg(orig="example")
        >>> contents = '{"name": "John", "age": 30, "city": "New York"}'
        >>> result = load_json(arg, contents)
        >>> print(result)
        {'name': 'John', 'age': 30, 'city': 'New York'}

    Note:
        - The function assumes that the input string `contents` is a valid JSON formatted string. If the input is not valid JSON, this function may raise an exception.
        - Ensure you have imported the necessary modules and defined the custom class `JsonDictPreservingDuplicateKeys` before using this function.
    """
    try:
        return json.loads(contents, object_pairs_hook=lambda x: JsonDictPreservingDuplicateKeys(x))
    except ValueError as e:
        raise ParseError(f'{arg.orig!r}: {e}')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_requestitems_load_json_0_test_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_load_json_0_test_none_input.py:6:50: E0602: Undefined variable 'JSONType' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_load_json_0_test_none_input.py:36:64: E0602: Undefined variable 'JsonDictPreservingDuplicateKeys' (undefined-variable)


"""