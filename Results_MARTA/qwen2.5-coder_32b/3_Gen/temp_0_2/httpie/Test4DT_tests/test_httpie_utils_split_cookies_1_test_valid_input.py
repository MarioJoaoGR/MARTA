
import pytest
from httpie.utils import split_cookies

# Mocking the necessary module and its function if needed
@pytest.mark.parametrize("input_string, expected", [
    ('cookie1=value1, cookie2=value2', ['cookie1=value1', 'cookie2=value2']),
    ('; path=/; domain=.example.com; Secure', ['; path=/; domain=.example.com; Secure']),
    ('', [])
])
def test_split_cookies(input_string, expected):
    assert split_cookies(input_string) == expected
