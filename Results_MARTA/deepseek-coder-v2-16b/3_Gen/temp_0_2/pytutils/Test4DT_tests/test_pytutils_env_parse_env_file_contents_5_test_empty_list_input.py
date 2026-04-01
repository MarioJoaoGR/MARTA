
import pytest
from pytutils.env import parse_env_file_contents

def test_empty_list_input():
    lines = []
    result = list(parse_env_file_contents(lines))
    assert result == []
