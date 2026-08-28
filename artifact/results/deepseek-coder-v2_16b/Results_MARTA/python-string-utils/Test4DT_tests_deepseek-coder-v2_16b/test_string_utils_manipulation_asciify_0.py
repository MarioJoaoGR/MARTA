
import pytest
from string_utils.manipulation import asciify
from string_utils.errors import InvalidInputError

# Helper function to simulate is_string check for testing purposes
def is_string(obj):
    return isinstance(obj, str)

class TestAsciify:
    
    def test_valid_input(self):
        input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
        expected_output = 'eeuuooaaeynAAACIINOE'
        assert asciify(input_string) == expected_output
    
    def test_valid_ascii_input(self):
        input_string = 'hello world'
        expected_output = 'hello world'
        assert asciify(input_string) == expected_output
    
    def test_invalid_input(self):
        input_string = 12345
        with pytest.raises(InvalidInputError):
            asciify(input_string)
