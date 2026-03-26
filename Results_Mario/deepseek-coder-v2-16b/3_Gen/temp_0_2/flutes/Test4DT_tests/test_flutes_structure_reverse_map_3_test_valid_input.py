
from typing import Dict, List
import pytest
from flutes.structure import reverse_map  # Assuming this is the correct module path

@pytest.fixture
def valid_input():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    return word_to_id

def test_valid_input(valid_input):
    id_to_word = reverse_map(valid_input)
    assert id_to_word == ['a', 'aardvark', 'abandon']
