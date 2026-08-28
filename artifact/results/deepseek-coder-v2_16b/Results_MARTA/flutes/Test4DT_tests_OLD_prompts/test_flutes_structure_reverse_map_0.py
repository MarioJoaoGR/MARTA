
import pytest
from typing import Dict, List, TypeVar
from unittest.mock import patch
from flutes.structure import reverse_map

T = TypeVar('T')

def test_reverse_map_basic():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {'a': 0, 'aardvark': 1, 'abandon': 2}
    with patch('builtins.sorted') as mock_sorted:
        mock_sorted.return_value = list(word_to_id.items())
        id_to_word = reverse_map(word_to_id)
        assert words == id_to_word, f"Expected {words}, but got {id_to_word}"

def test_reverse_map_empty():
    empty_dict = {}
    with patch('builtins.sorted') as mock_sorted:
        mock_sorted.return_value = list(empty_dict.items())
        id_to_word = reverse_map(empty_dict)
        assert [] == id_to_word, f"Expected [], but got {id_to_word}"

def test_reverse_map_large():
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    with patch('builtins.sorted') as mock_sorted:
        mock_sorted.return_value = list(word_to_id.items())
        id_to_word = reverse_map(word_to_id)
        assert words == id_to_word, f"Expected {words}, but got {id_to_word}"
