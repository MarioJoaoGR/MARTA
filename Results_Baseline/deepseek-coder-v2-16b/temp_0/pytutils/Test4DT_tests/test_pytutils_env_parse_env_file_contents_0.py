
import pytest
import typing
from pytutils.env import parse_env_file_contents

# Test cases for parse_env_file_contents function

def test_default_usage():
    generator = parse_env_file_contents([])  # Provide a default empty list
    assert list(generator) == [], "Expected an empty iterable when no lines are provided"

def test_with_input_lines():
    lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    generator = parse_env_file_contents(lines)
    expected_output = [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]