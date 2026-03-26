
import pytest
from string_utils.manipulation import asciify

def test_valid_input():
    # Test with a Unicode string containing various non-ASCII characters
    result = asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')
    assert result == 'eeuuooaaeynAAACIINOE'
