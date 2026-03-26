
import os
from isort.deprecated.finders import chdir
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        with chdir(None) as cm:
            pass
