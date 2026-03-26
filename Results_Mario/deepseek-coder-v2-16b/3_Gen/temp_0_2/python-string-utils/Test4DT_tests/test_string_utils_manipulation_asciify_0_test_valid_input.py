
import pytest
from string_utils.manipulation import asciify

def test_valid_input():
    # Test case with various non-ASCII characters
    result = asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
    assert result == 'eeuuooaaeynAAACIINOE'
    
    # Test case with ASCII characters only
    result_ascii_only = asciify('hello world')
    assert result_ascii_only == 'hello world'
