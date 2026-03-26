
import unicodedata
from string_utils.manipulation import is_string, InvalidInputError

def asciify(input_string: str) -> str:
    """
    Force string content to be ascii-only by translating all non-ascii chars into the closest possible representation
    (eg: ó -> o, Ë -> E, ç -> c...).

    **Bear in mind**: Some chars may be lost if impossible to translate.

    *Example:*

    >>> asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') # returns 'eeuuooaaeynAAACIINOE'

    :param input_string: String to convert
    :return: Ascii utf-8 string
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    # "NFKD" is the algorithm which is able to successfully translate the most of non-ascii chars
    normalized = unicodedata.normalize('NFKD', input_string)

    # encode string forcing ascii and ignore any errors (unrepresentable chars will be stripped out)
    ascii_bytes = normalized.encode('ascii', 'ignore')

    # turns encoded bytes into an utf-8 string
    ascii_string = ascii_bytes.decode('utf-8')

    return ascii_string

# Test for empty string input
def test_empty_string():
    assert asciify("") == ""
