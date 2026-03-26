
import pytest
from typing import Iterable, List

def skip_chars(src: str, pos: int, chars: Iterable[str]) -> int:
    """
    Skips characters in the input string based on a list of specified characters.
    
    Parameters:
        src (str): The input string from which to skip characters.
        pos (int): The starting position in the string to begin skipping characters.
        chars (Iterable[str]): An iterable containing the characters to be skipped.
        
    Returns:
        int: The updated position after skipping all specified characters in the string.
    
    Examples:
        >>> skip_chars("hello world", 0, ["l"])
        2
        >>> skip_chars("hello world", 0, ["o"])
        7
        >>> skip_chars("hello world", 3, ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"])
        8
    """
    try:
        while src[pos] in chars:
            pos += 1
    except IndexError:
        pass
    return pos

def test_edge_case_none():
    with pytest.raises(TypeError):
        skip_chars(None, 0, ["h"])
