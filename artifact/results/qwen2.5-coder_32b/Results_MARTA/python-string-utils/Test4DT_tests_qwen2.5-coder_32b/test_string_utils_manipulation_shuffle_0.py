
import random
from string_utils.manipulation import shuffle

# Set a fixed seed for reproducibility in tests
random.seed(42)




def test_shuffle_with_empty_string():
    result = shuffle('')
    assert result == ''  # An empty string should remain unchanged

def test_shuffle_with_single_character_string():
    result = shuffle('a')
    assert result == 'a'  # A single character string should remain unchanged