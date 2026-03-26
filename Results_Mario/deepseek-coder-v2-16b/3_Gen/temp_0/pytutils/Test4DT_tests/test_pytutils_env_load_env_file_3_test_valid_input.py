
import pytest
from pytutils.env import load_env_file, parse_env_file_contents, expand
import os
import collections
import typing

@pytest.fixture
def setup():
    return {'lines': ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']}

def test_valid_input(setup):
    lines = setup["lines"]
    result = load_env_file(lines, write_environ=dict())
    
    expected = collections.OrderedDict([
        ('TEST', f'{os.path.expanduser("~")}/yeee-{os.getenv("PATH", "")}'),
        ('THISIS', os.path.expanduser("~/a/test")),
        ('YOLO', os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))
    ])
    
    assert result == expected
