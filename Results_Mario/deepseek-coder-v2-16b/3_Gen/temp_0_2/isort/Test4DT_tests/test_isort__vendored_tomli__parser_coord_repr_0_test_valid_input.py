
import pytest

def coord_repr(src: str, pos: int) -> str:
    """
    Generate a string representation of the line and column number for a given position in a source code string.

    Parameters:
        src (str): The source code as a string.
        pos (int): The position within the source code string where the coordinate representation is needed.

    Returns:
        str: A string representing the line and column number of the given position in the source code. If the position 
             is beyond the end of the document, it returns "end of document".

    Examples:
        >>> coord_repr("hello\nworld", 0)
        'line 1, column 1'
        
        >>> coord_repr("hello\nworld", 6)
        'line 2, column 1'
        
        >>> coord_repr("hello\nworld", 7)
        'line 2, column 2'
        
        >>> coord_repr("hello\nworld", 100)
        'end of document'

    The function calculates the line and column number by counting the newlines in the source code up to the given position.
    If the position is at the beginning of a line, it sets the column number as 1 plus the position index. Otherwise, it calculates
    the column number based on the distance from the last newline before the position.
    
    This function is designed to provide a clear and concise representation of where in the source code a specific position falls,
    aiding in debugging and understanding the structure of large codebases. It ensures that even for positions beyond typical line breaks,
    users can still get meaningful information about their location within the document.
    """
    if pos >= len(src):
        return "end of document"
    line = src.count("\n", 0, pos) + 1
    if line == 1:
        column = pos + 1
    else:
        column = pos - src.rindex("\n", 0, pos)
    return f"line {line}, column {column}"

@pytest.mark.parametrize("src, pos, expected", [
    ("hello\nworld", 0, "line 1, column 1"),
    ("hello\nworld", 6, "line 2, column 1"),
    ("hello\nworld", 7, "line 2, column 2"),
    ("hello\nworld", 100, "end of document")
])
def test_valid_input(src, pos, expected):
    assert coord_repr(src, pos) == expected
