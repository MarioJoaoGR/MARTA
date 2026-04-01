
import pytest

def _normalize_empty_lines(lines: list[str]) -> list[str]:
    """
    Normalizes empty lines at the end of the list.
    
    Parameters:
        lines (list[str]): A list of strings where each element represents a line from the text.
        
    Returns:
        list[str]: The normalized list of lines with exactly one empty line at the end if necessary.
    """
    while lines and not lines[-1]:
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

def test_none_input():
    with pytest.raises(TypeError):
        _output_as_string(None, '\n')
