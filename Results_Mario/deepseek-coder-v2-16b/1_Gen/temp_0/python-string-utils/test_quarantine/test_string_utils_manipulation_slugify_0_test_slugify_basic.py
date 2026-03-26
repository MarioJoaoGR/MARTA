
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

# Test case for basic functionality
def test_slugify_basic():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_0_test_slugify_basic.py F [100%]

=================================== FAILURES ===================================
______________________________ test_slugify_basic ______________________________

    def test_slugify_basic():
        assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
>       assert slugify('Mönstér Mägnët') == 'monster-magnet'
E       AssertionError: assert 'm-nst-r-m-gn-t' == 'monster-magnet'
E         
E         - monster-magnet
E         + m-nst-r-m-gn-t

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_0_test_slugify_basic.py:45: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_0_test_slugify_basic.py::test_slugify_basic
============================== 1 failed in 0.03s ===============================

"""