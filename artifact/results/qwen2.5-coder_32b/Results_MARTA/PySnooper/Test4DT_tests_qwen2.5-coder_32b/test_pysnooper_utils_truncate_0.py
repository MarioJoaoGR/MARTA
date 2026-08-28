
import pytest

def truncate(string, max_length):
    if (max_length is None) or (len(string) <= max_length):
        return string
    else:
        left = (max_length - 3) // 2
        right = max_length - 3 - left
        return u'{}...{}'.format(string[:left], string[-right:])

def test_truncate_basic():
    assert truncate("Hello, world!", 10) == "Hel...rld!"
    assert truncate("Short", 10) == "Short"
    assert truncate("Another example", None) == "Another example"
