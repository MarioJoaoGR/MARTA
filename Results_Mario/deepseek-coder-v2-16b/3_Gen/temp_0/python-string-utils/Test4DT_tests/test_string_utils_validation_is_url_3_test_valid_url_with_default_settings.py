
import pytest
from string_utils.validation import is_url

@pytest.mark.parametrize("input_string, expected", [
    ('http://www.mysite.com', True),
    ('https://mysite.com', True),
    ('.mysite.com', False),
    ('ftp://example.com', True)  # Assuming 'ftp' is allowed scheme
])
def test_valid_url_with_default_settings(input_string, expected):
    assert is_url(input_string) == expected
