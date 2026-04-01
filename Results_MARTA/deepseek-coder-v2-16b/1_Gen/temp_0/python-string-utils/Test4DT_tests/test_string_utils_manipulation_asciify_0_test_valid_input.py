
import pytest
from string_utils.manipulation import asciify

def test_valid_input():
    # Test with a valid input string containing non-ASCII characters
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    
    # Test with a valid input string containing only ASCII characters
    assert asciify('hello world') == 'hello world'
