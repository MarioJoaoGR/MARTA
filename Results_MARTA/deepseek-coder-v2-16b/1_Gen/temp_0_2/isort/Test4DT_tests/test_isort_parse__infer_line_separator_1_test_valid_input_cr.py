
import pytest

def _infer_line_separator(contents: str) -> str:
    """
    Infers the line separator used in a given string.

    This function takes a single argument, `contents`, which is expected to be a string containing text. The function checks for common line separators (\r\n, \r, and \n) within the provided string and returns the detected line separator. If none of these are found, it defaults to returning "\n".

    Parameters:
        contents (str): A string that may contain multiple lines separated by '\r\n', '\r', or '\n'.

    Returns:
        str: The inferred line separator from the input string. It will be one of '\r\n', '\r', or '\n'. If none are detected, it returns '\n'.

    Examples:
        >>> _infer_line_separator("Hello\r\nWorld")
        '\r\n'
        
        >>> _infer_line_separator("Hello\rWorld")
        '\r'
        
        >>> _infer_line_separator("Hello\nWorld")
        '\n'
        
        >>> _infer_line_separator("HelloWorld")
        '\n'
    """
    if "\r\n" in contents:
        return "\r\n"
    if "\r" in contents:
        return "\r"
    return "\n"

def test_valid_input_cr():
    assert _infer_line_separator("Hello\rWorld") == '\r'
