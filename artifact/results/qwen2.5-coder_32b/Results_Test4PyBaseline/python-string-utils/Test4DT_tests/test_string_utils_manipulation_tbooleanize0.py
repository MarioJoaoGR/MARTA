
# Importing the booleanize function from string_utils module
from string_utils import booleanize

def test_booleanize_whitespace_handling():
    assert booleanize(' true '.strip()) is True
    assert booleanize(' yes '.strip()) is True
    assert booleanize(' 1 '.strip()) is True
    assert booleanize(' y '.strip()) is True
    assert booleanize(' false '.strip()) is False
    assert booleanize(' nope '.strip()) is False
