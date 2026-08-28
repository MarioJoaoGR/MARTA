
import random
from string_utils.manipulation import shuffle, InvalidInputError

def test_valid_case():
    input_string = 'hello world'
    shuffled_result = shuffle(input_string)
    assert len(shuffled_result) == len(input_string), "Shuffled result length does not match the original"
    assert set(shuffled_result) == set(input_string), "Shuffled result contains different characters than the original"

def test_edge_cases():
    # Test with an empty string
    input_string = ''
    shuffled_result = shuffle(input_string)
    assert shuffled_result == '', "Shuffling an empty string should return an empty string"
    
    # Test with a single character string
    input_string = 'a'
    shuffled_result = shuffle(input_string)
    assert shuffled_result == 'a', "Shuffling a single character string should return the same string"

def test_invalid_input():
    invalid_inputs = [123, None, [1, 2, 3], {'key': 'value'}]
    
    for input_value in invalid_inputs:
        try:
            shuffle(input_value)
        except InvalidInputError as e:
            assert str(e) == f'Expected "str", received "{type(input_value).__name__}"', f"Incorrect error message for input {input_value}"
        else:
            assert False, f"Shuffle did not raise an error for invalid input: {input_value}"
