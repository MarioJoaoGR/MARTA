
import pytest
from string_utils.manipulation import asciify

def test_valid_input():
    # Test with a string containing only ASCII characters
    assert asciify('hello world') == 'hello world'
    
    # Test with a string containing non-ASCII characters
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
