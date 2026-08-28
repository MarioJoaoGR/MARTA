
import pytest
import codecs
import re

# Define a regular expression for matching Unicode escape sequences
_ESCAPE_SEQUENCE_RE = re.compile(r'\\u([0-9A-Fa-f]{4})')

def _decode_escapes(s):
    def decode_match(match):
        return codecs.decode(match.group(0), 'unicode-escape')

    return _ESCAPE_SEQUENCE_RE.sub(decode_match, s)

# Test case for decoding Unicode escape sequences in a string
def test_decode_escapes():
    input_string = "Hello\u00A9 World!"
    expected_output = "Hello© World!"
    assert _decode_escapes(input_string) == expected_output
