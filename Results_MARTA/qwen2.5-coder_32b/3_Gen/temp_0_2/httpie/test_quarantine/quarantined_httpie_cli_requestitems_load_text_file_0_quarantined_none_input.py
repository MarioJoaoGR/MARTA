
import os
from httpie.cli.requestitems import KeyValueArg
from httpie.exceptions import ParseError
import unittest.mock as mock

def load_text_file(item: KeyValueArg) -> str:
    """
    Loads and returns the contents of a text file specified by the given path.

    Parameters:
        item (KeyValueArg): An object containing the path to the text file as its value, 
                            along with its original representation for error messages.

    Returns:
        str: The decoded content of the text file.

    Raises:
        ParseError: If there is an issue with reading or decoding the file, including if the file cannot be found or read, 
                    or if the content cannot be decoded as UTF-8 (which is typical for text files).
    """
    path = item.value
    try:
        with open(os.path.expanduser(path), 'rb') as f:
            return f.read().decode()
    except OSError as e:
        raise ParseError(f'{item.orig!r}: {e}')
    except UnicodeDecodeError:
        raise ParseError(
            f'{item.orig!r}: cannot embed the content of {item.value!r},'
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_requestitems_load_text_file_0_test_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_load_text_file_0_test_none_input.py:4:0: E0401: Unable to import 'httpie.exceptions' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_requestitems_load_text_file_0_test_none_input.py:4:0: E0611: No name 'exceptions' in module 'httpie' (no-name-in-module)


"""