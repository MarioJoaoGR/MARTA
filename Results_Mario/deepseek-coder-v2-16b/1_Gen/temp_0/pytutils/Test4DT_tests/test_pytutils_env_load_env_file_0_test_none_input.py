
import os
import typing
import collections
from pytutils.env import load_env_file
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        load_env_file(None)
