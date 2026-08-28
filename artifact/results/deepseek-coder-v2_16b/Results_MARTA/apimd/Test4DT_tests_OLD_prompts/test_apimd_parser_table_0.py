
import pytest
from apimd.parser import table
from typing import Iterable, Union

def test_valid_input():
    with pytest.raises(TypeError):
        table('Name', 'Age', [['Alice', '25'], ['Bob', '30']])
