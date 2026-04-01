
import pytest
from superstring.superstring import SuperStringConcatenation, SuperStringSubstring

def test_invalid_input():
    left_substr = SuperStringSubstring('Hello', 0, 5)
    right_substr = SuperStringSubstring('World!', 0, 5)
    concatenated = SuperStringConcatenation(left_substr, right_substr)
    invalid_index = 'invalid'
    
    with pytest.raises(TypeError):
        concatenated.character_at(invalid_index)
