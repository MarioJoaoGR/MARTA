
from typing import Iterable, Pos

def skip_chars(src: str, pos: Pos, chars: Iterable[str]) -> Pos:
    """
    Skips characters in a string based on a set of specified characters.

    Parameters:
        src (str): The input string from which characters will be skipped.
        pos (Pos): The current position in the string to start skipping characters from. This should be an instance of a class that supports indexing and incrementation, such as `int` or a custom class implementing these functionalities.
        chars (Iterable[str]): An iterable containing the set of characters to skip.

    Returns:
        Pos: The updated position in the string after skipping all specified characters. If the end of the string is reached before any character from `chars` is encountered, the function will return the current position unchanged.

    Examples:
        To use this function, you would typically call it with a string and a starting position, along with an iterable containing the characters to skip. For example:
        
        ```python
        result = skip_chars("hello world", 0, ["l", "o"])
        print(result)  # Output will be 5 because 'l' is skipped until 'o', then it stops at index 5
        ```

        In this example, the function skips all occurrences of 'l' and 'o' in the string "hello world" starting from position 0. The result is that the function returns 5 as the new position after skipping these characters.

    Notes:
        - Ensure that `pos` is a valid index within the bounds of `src`. If `pos` is out of range, an IndexError will be raised when attempting to access `src[pos]`.
        - The function does not modify the original string or position; it only returns the updated position after skipping characters.
        - This function can handle any iterable containing strings as elements for `chars`, allowing flexibility in specifying which characters to skip.
    """
    try:
        while src[pos] in chars:
            pos += 1
    except IndexError:
        pass
    return pos

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling.py:2:0: E0611: No name 'Pos' in module 'typing' (no-name-in-module)


"""