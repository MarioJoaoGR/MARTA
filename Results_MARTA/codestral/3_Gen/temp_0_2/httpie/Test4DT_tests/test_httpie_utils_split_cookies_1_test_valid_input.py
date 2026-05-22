
import pytest
from httpie.utils import split_cookies

def test_split_cookies_valid_input():
    # Test with valid input containing multiple cookies separated by ', '
    assert split_cookies('cookie1=value1, cookie2=value2') == ['cookie1=value1', 'cookie2=value2']
    
    # Test with a single cookie string that contains '; ' which should not be split
    assert split_cookies('; path=/; domain=.example.com; Secure') == ['; path=/; domain=.example.com; Secure']
    
    # Test with an empty input, expecting an empty list
    assert split_cookies('') == []
