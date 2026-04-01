
import unicodedata
from string_utils.manipulation import asciify

def test_valid_input():
    # Test with various non-ASCII characters
    assert asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË') == 'eeuuooaaeynAAACIINOE'
    
    # Test with a string containing only ASCII characters
    assert asciify('hello world') == 'hello world'
    
    # Additional test to ensure it handles empty strings correctly
    assert asciify('') == ''
