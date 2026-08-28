
import pytest
from unittest.mock import patch
from mimesis.random import Random


def test_invalid_input():
    rand_gen = Random()
    with patch('mimesis.random.Random.choice', side_effect=['a', 'b', 'c']):
        with pytest.raises(RuntimeError):
            rand_gen.generate_string("xyz", 5)
