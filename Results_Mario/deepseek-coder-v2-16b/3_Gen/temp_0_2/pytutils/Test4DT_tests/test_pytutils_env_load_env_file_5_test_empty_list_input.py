
import os
import typing
import collections
from pytutils.env import load_env_file

def test_empty_list_input():
    lines = []
    result = load_env_file(lines)
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 0
