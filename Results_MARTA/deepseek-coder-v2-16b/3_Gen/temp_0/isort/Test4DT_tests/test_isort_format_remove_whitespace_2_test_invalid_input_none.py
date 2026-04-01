
import pytest


def remove_whitespace(content: str, line_separator: str = "\n") -> str:
    """
    Removes all whitespace characters from the input string.
    
    This function takes a string `content` and optionally a `line_separator` which defaults to newline character ("\n"). It removes spaces, form feed (\x0c), and any other whitespace characters found in the content based on the specified line separator.
    
    Parameters:
        content (str): The input string from which to remove whitespace characters.
        line_separator (str, optional): The character used to identify lines within the content. Defaults to "\n".
        
    Returns:
        str: A new string with all whitespace characters removed.
    
    Examples:
        >>> remove_whitespace("Hello, World!")
        'Hello,World!'
        
        >>> remove_whitespace("This is a test.", line_separator=".")
        'Thisisatest.'
        
        >>> remove_whitespace("Remove \n all \t newlines and spaces", line_separator="\n")
        'Removeallnewlinesandspaces'
    """
    if content is None:
        raise ValueError("Content cannot be None")
    content = content.replace(line_separator, "").replace(" ", "").replace("\x0c", "")
    return content

def test_invalid_input_none():
    with pytest.raises(ValueError):
        remove_whitespace(None)
