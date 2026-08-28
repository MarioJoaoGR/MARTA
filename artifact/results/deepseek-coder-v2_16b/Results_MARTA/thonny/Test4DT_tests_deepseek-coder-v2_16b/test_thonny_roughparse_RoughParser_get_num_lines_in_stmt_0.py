
import pytest
from thonny.roughparse import RoughParser

def test_invalid_initialization_none_args():
    with pytest.raises(TypeError):
        RoughParser()
