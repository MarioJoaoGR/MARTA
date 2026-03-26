
import pytest
import os
import typing
import collections
from pytutils.env import load_env_file, parse_env_file_contents, expand

def test_none_input():
    with pytest.raises(TypeError):
        load_env_file(None)
