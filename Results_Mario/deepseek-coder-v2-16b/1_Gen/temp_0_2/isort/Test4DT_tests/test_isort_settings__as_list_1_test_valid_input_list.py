
import pytest
from isort.settings import _as_list  # Assuming this is the correct module path for _as_list

def test_valid_input_list():
    assert _as_list("apple, banana, cherry") == ['apple', 'banana', 'cherry']
    assert _as_list([" apple ", " banana ", " cherry "]) == ['apple', 'banana', 'cherry']
    assert _as_list("apple\nbanana\ncherry") == ['apple', 'banana', 'cherry']
