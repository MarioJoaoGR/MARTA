
import argparse
import pytest
from your_module import add_tasknoplay_options  # Replace 'your_module' with the actual module name where this function is defined

# Define a simple default value for testing
C = type('Constants', (), {'TASK_TIMEOUT': 60})

@pytest.fixture(scope="module")
def parser():
    parser = argparse.ArgumentParser(description="Your program description")
    add_tasknoplay_options(parser)
    return parser

# Test scenario 1: test_valid_input
def test_valid_input(parser):
    args = parser.parse_args(['--task-timeout', '300'])
    assert args.task_timeout == 300

# Test scenario 2: test_edge_case
def test_edge_case(parser):
    args = parser.parse_args([])
    assert args.task_timeout == C.TASK_TIMEOUT

# Test scenario 3: test_invalid_input
def test_invalid_input(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(['--task-timeout', '0'])
    with pytest.raises(SystemExit):
        parser.parse_args(['--task-timeout', '-1'])
    with pytest.raises(SystemExit):
        parser.parse_args(['--task-timeout', 'abc'])
