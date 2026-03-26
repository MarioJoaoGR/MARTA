
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    with pytest.raises(TypeError):
        meta_set.update(123)  # Providing a non-iterable object to ensure it raises an appropriate error
