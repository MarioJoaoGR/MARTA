
import subprocess

import pytest

from isort.hooks import get_lines


def test_get_lines_basic():
    result = get_lines(['ls', '-l'])
    assert isinstance(result, list), "Expected a list of strings"
    for line in result:
        assert isinstance(line, str), "Each line should be a string"
        # Simplified assertion to check if the line contains any whitespace