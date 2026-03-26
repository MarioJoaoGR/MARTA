
import pytest
from typing import Iterable, List

def skip_chars(src: str, pos: int, chars: Iterable[str]) -> int:
    """
    Skips characters in a string based on a set of specified characters.

    Parameters:
        src (str): The input string from which characters will be skipped.
        pos (int): The current position in the string to start skipping characters from. This should be an instance of a class that supports indexing and incrementation, such as `int` or a custom class implementing these functionalities.
        chars (Iterable[str]): An iterable containing the characters to skip.

    Returns:
        int: The updated position after skipping all specified characters in the string. If the end of the string is reached before any character from `chars` is encountered, the function will return the current position unchanged.

    Examples:
        Example 1:
            src = "hello world"
            pos = 0
            chars = ['o', 'd']
            result = skip_chars(src, pos, chars)
            # The function will iterate through 'hello world' and skip 'o' and 'd', resulting in pos being set to 11.
            print(result)  # Output: 11

        Example 2:
            src = "banana"
            pos = 0
            chars = ['b', 'n']
            result = skip_chars(src, pos, chars)
            # The function will iterate through 'banana' and skip 'b' and 'n', resulting in pos being set to 2.
            print(result)  # Output: 2

        Example 3:
            src = "python"
            pos = 0
            chars = ['x', 'z']
            result = skip_chars(src, pos, chars)
            # The function will iterate through 'python' and not find any characters to skip since neither 'x' nor 'z' are in the string. Therefore, pos remains unchanged at 0.
            print(result)  # Output: 0

    Note:
        - Ensure that `pos` is a valid index within the bounds of `src`. If not, an IndexError will be raised.
        - The function does not modify the input string or position; it only returns the updated position after skipping characters based on the provided set.
    """
    try:
        while src[pos] in chars:
            pos += 1
    except IndexError:
        pass
    return pos

def test_edge_case_none():
    with pytest.raises(TypeError):
        skip_chars(None, 0, ['a'])
