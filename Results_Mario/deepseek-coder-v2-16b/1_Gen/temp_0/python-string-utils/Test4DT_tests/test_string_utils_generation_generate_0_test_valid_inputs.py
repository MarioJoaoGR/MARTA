
import pytest
from string_utils.generation import roman_encode

def test_valid_inputs():
    def generate(start, stop, step):
        current = start
        while current != stop:
            yield roman_encode(current)
            current += step
        yield roman_encode(current)
    
    # Test case 1: Start at 1, stop at 5, step of 1
    result = list(generate(1, 5, 1))
    assert result == ['I', 'II', 'III', 'IV', 'V']

    # Test case 2: Start at 3, stop at 7, step of 2
    result = list(generate(3, 7, 2))
    assert result == ['III', 'V', 'VII']

    # Test case 3: Start at 10, stop at 14, step of 1
    result = list(generate(10, 14, 1))
    assert result == ['X', 'XI', 'XII', 'XIII', 'XIV']
