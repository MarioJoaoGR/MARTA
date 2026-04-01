
import pytest
from string_utils.generation import random_string
import random
import string

def test_edge_case_zero():
    with pytest.raises(ValueError):
        random_string(0)
