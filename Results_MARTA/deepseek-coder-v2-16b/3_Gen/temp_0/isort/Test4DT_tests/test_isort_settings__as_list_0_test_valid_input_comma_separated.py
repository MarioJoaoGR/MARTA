
import pytest

from isort.settings import _as_list


def test_valid_input_comma_separated():
    assert _as_list("apple, banana, orange") == ['apple', 'banana', 'orange']
    assert _as_list("apple\nbanana\norange") == ['apple', 'banana', 'orange']
    assert _as_list("apple, banana,, orange,") == ['apple', 'banana', 'orange']
    assert _as_list("") == []
