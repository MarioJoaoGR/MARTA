
from string_utils import asciify

def test_asciify_with_only_non_ascii_chars():
    assert asciify('ßøå') == 'a'
