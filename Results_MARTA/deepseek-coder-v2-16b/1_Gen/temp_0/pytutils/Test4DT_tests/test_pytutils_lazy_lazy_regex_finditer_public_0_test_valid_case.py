
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def finditer_public(pattern, string, flags=0):
    """
    Searches for all occurrences of a given pattern in the provided string using a regular expression.
    
    This function accepts three parameters:
    
    - `pattern`: A string representing the regular expression pattern to search for. It can be either a standard string or an instance of LazyRegex class, which is designed to delay compilation until it's needed.
    - `string`: The input string in which to search for occurrences of the pattern.
    - `flags` (optional): An integer representing bitwise flags that modify the behavior of the regular expression search. These can include options like IGNORECASE for case-insensitive matching, MULTILINE for multiline matching, etc. Default is 0, meaning no special flags are applied.
    
    The function returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string. If a LazyRegex instance is provided as the pattern, it will be used directly to find iterators; otherwise, the pattern is compiled using Python's built-in regular expression module and then used for searching.
    
    Examples:
    
    Basic usage with a standard regex pattern:
        >>> result = finditer_public(r'\d+', '123abc456')
        >>> for match in result:
        ...     print(match.group())
        123
        456
    
    Using the function with a LazyRegex instance:
        >>> lazy_pattern = LazyRegex(r'\d+')
        >>> result = finditer_public(lazy_pattern, '123abc456')
        >>> for match in result:
        ...     print(match.group())
        123
        456
    
    Note: The function assumes that the input string is a valid UTF-8 encoded string and that the pattern is a valid regular expression. Invalid inputs may lead to undefined behavior or exceptions.
    """
    if isinstance(pattern, LazyRegex):
        return pattern.finditer(string)
    else:
        import re
        real_re = re.compile(pattern, flags)
        return real_re.finditer(string)

# Test case for the function finditer_public
def test_valid_case():
    # Define a pattern and a string to search in
    pattern = r'\d+'
    string = '123abc456'
    
    # Call the function with the defined pattern and string
    result = finditer_public(pattern, string)
    
    # Initialize an empty list to store the matched groups
    matched_groups = []
    
    # Iterate over the match objects in the result and collect the group() values
    for match in result:
        matched_groups.append(match.group())
    
    # Define the expected matched groups
    expected_matched_groups = ['123', '456']
    
    # Assert that the matched groups are equal to the expected matched groups
    assert matched_groups == expected_matched_groups
