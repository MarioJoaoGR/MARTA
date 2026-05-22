
import pytest
from httpie.utils import split_cookies

def test_none_input():
    assert split_cookies('') == []
