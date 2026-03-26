
import re
from dataclasses_json.stringcase import uplowcase

def camelcase(string):
    """ Convert string into camel case.

    Args:
        string: String to convert.

    Returns:
        string: Camel case string.

    """

    string = re.sub(r"^[\-_\.]", '', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[\-_\.\s]([a-z0-9])",
                     lambda matched: uplowcase(matched.group(1), 'up'),
                     string[1:]))

import pytest

def test_empty_string():
    assert camelcase("") == ""
