
import pytest
from pytutils.env import parse_env_file_contents
import re
import typing

def test_empty_list_input():
    lines = []
    parser = parse_env_file_contents(lines)
    assert list(parser) == []
