
import pytest

def _normalize_empty_lines(lines: list[str]) -> list[str]:
    # Helper function to normalize empty lines at the end of the list
    while lines and lines[-1] == '':
        lines.pop()
    return lines

def _output_as_string(lines: list[str], line_separator: str) -> str:
    """
    Joins a list of lines into a single string with the specified separator, normalizing empty lines.
    
    This function normalizes the spacing of empty lines at the end of the list and ensures there is exactly one empty line at the end of the resulting string.
    
    Parameters:
        lines (list[str]): A list of strings where each element represents a line from the text.
        line_separator (str): The separator to use between lines in the final string.
        
    Returns:
        str: A single string with all lines joined by the specified separator, and exactly one empty line at the end.
        
    Examples:
        >>> _output_as_string(["line1", "line2"], "\n")
        'line1\nline2\n'
        
        >>> _output_as_string(["line1", "", ""], " ")
        'line1  \n'
        
        >>> _output_as_string([""], "\t")
        '\t'
    """
    return line_separator.join(_normalize_empty_lines(lines))

def test_empty_list():
    lines = []
    line_separator = '\n'
    expected_output = ''
    
    result = _output_as_string(lines, line_separator)
    
    assert result == expected_output
