
import pytest
from string_utils.manipulation import shuffle, InvalidInputError
import random

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        assert shuffle(None)  # This should raise an InvalidInputError
