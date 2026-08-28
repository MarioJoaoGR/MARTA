# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import shuffle, InvalidInputError

def test_shuffle_with_normal_string():
    original = 'hello world'
    shuffled = shuffle(original)
    assert len(shuffled) == len(original), "Shuffled string length should match the original"
    assert set(shuffled) == set(original), "Shuffled string should contain the same characters as the original"

def test_shuffle_with_empty_string():
    result = shuffle('')
    assert result == '', "Shuffling an empty string should return an empty string"

def test_shuffle_with_single_character_string():
    result = shuffle('a')
    assert result == 'a', "Shuffling a single character string should return the same string"

def test_shuffle_with_numeric_string():
    original = '1234567890'
    shuffled = shuffle(original)
    assert len(shuffled) == len(original), "Shuffled numeric string length should match the original"
    assert set(shuffled) == set(original), "Shuffled numeric string should contain the same characters as the original"

def test_shuffle_with_special_characters():
    original = '!@#$%^&*()'
    shuffled = shuffle(original)
    assert len(shuffled) == len(original), "Shuffled special character string length should match the original"
    assert set(shuffled) == set(original), "Shuffled special character string should contain the same characters as the original"

def test_shuffle_with_non_string_input():
    with pytest.raises(InvalidInputError):
        shuffle(123)

def test_shuffle_with_none_input():
    with pytest.raises(InvalidInputError):
        shuffle(None)

def test_shuffle_with_list_input():
    with pytest.raises(InvalidInputError):
        shuffle(['h', 'e', 'l', 'l', 'o'])

def test_shuffle_with_dict_input():
    with pytest.raises(InvalidInputError):
        shuffle({'key': 'value'})

def test_shuffle_with_tuple_input():
    with pytest.raises(InvalidInputError):
        shuffle(('h', 'e', 'l', 'l', 'o'))
