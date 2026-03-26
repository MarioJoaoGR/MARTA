
import pytest
from pytutils.sets import MetaSet

def test_invalid_input_none():
    ms = MetaSet()
    with pytest.raises(TypeError):
        ms.update(None)
