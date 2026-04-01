
import pytest

def coord_repr(src: str, pos: int) -> str:
    """
    Generate a string representation of the line and column number for a given position in a source code string.

    Parameters:
        src (str): The source code as a string.
        pos (int): The position within the source code string where the coordinates are to be determined.

    Returns:
        str: A string representation of the line and column number, formatted as "line X, column Y".
            If the position is beyond the end of the document, it returns "end of document".

    Examples:
        >>> coord_repr("hello\nworld", 5)
        'line 2, column 1'
        
        >>> coord_repr("hello\nworld", 6)
        'line 2, column 2'
        
        >>> coord_repr("hello\nworld", 7)
        'line 2, column 3'
        
        >>> coord_repr("hello\nworld", 100)
        'end of document'

    Notes:
        - The function assumes that the position is a valid index within the source code string.
        - The line number starts from 1, and the column number is zero-based but adjusted to be positive if it represents an offset from the end of a line.
    
    Generates a string representation of the position in the source code where `pos` is within `src`.

    Parameters:
        src (str): The source code as a string.
        pos (Pos): The position within the source code.

    Returns:
        str: A string describing the line and column number where `pos` is located in `src`. If `pos` is beyond the end of the document, it returns "end of document".

    Usage:
        This function is used to provide a human-readable description of the position within the source code. It can be useful for debugging or logging purposes when dealing with large codebases.
    """
    if pos >= len(src):
        return "end of document"
    line = src.count("\n", 0, pos) + 1
    if line == 1:
        column = pos + 1
    else:
        column = pos - src.rindex("\n", 0, pos)
    return f"line {line}, column {column}"

def test_edge_case_end_of_document():
    assert coord_repr("hello\nworld", 100) == "end of document"
