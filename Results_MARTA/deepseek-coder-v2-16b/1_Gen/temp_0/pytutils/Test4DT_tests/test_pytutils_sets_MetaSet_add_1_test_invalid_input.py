
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    with pytest.raises(TypeError):
        meta_set.add({'key': 'value'})  # Invalid input type (dictionary)
