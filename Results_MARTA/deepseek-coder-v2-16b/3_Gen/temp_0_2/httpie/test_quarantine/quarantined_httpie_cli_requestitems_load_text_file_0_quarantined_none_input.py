
import os
from httpie.cli.requestitems import KeyValueArg
from httpie.exceptions import ParseError

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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_requestitems_load_text_file_0_test_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_requestitems_load_text_file_0_test_none_input.py:28:25: E0001: Parsing failed: ''(' was never closed (Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_requestitems_load_text_file_0_test_none_input, line 28)' (syntax-error)


"""