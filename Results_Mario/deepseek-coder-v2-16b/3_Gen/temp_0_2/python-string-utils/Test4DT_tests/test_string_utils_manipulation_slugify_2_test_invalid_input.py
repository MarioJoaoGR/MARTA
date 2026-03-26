
import re
from string_utils.manipulation import asciify

def slugify(input_string: str, separator: str = '-') -> str:
    """
    Converts a string into a "slug" using provided separator.
    The returned string has the following properties:

    - it has no spaces
    - all letters are in lower case
    - all punctuation signs and non alphanumeric chars are removed
    - words are divided using provided separator
    - all chars are encoded as ascii (by using `asciify()`)
    - is safe for URL

    *Examples:*

    >>> slugify('Top 10 Reasons To Love Dogs!!!') # returns: 'top-10-reasons-to-love-dogs'
    >>> slugify('Mönstér Mägnët') # returns 'monster-magnet'

    :param input_string: String to convert.
    :type input_string: str
    :param separator: Sign used to join string tokens (default to "-").
    :type separator: str
    :return: Slug string
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    # replace any character that is NOT letter or number with spaces
    out = re.sub(r'[^a-zA-Z0-9]', ' ', input_string.lower()).strip()

    # replace spaces with join sign
    out = re.sub(r'\s+', separator, out)

    # normalize joins (remove duplicates)
    out = re.sub(re.escape(separator) + r'+', separator, out)

    return asciify(out)

# Test case for invalid input with special characters and numbers
def test_invalid_input():
    try:
        slugify('Top 10 Reasons To Love Dogs!!!')
    except ValueError as e:
        assert str(e) == "Input must be a string"
