
from typing import Iterable

import pytest


def skip_chars(src: str, pos: int, chars: Iterable[str]) -> int:
    """
    Skips characters in a string based on a set of specified characters.

    Parameters:
        src (str): The input string from which characters will be skipped.
        pos (int): The current position in the string to start skipping characters from.
        chars (Iterable[str]): An iterable containing the set of characters to skip.

    Returns:
        int: The updated position in the string after skipping all specified characters. If the end of the string is reached before any character from `chars` is encountered, the function will return the current position unchanged.
    """
    try:
        while src[pos] in chars:
            pos += 1
    except IndexError:
        pass
    return pos

def test_edge_case_none():
    with pytest.raises(TypeError):
        skip_chars(src=None, pos=0, chars=['a'])
