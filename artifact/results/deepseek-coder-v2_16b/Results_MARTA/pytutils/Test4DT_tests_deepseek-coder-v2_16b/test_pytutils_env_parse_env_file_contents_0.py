
import pytest
from pytutils.env import parse_env_file_contents
import re
import typing


def test_parse_env_file_contents_empty():
    lines = []
    parsed_lines = list(parse_env_file_contents(lines))
    expected_output = []
    assert parsed_lines == expected_output
