
import pytest
from blib2to3.pgen2.tokenize import group

def test_group_with_none():
    with pytest.raises(TypeError):
        pattern = group(None)
