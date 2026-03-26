
import pytest
from isort.main import parse_args as isort_parse_args

@pytest.mark.parametrize("argv", [
    ["--float-to-top"],  # Single valid argument
    ["--order-by-type", "file1.py"],  # Valid arguments with file path
    ["--float-to-top", "--order-by-type"],  # Multiple valid arguments
])
def test_valid_inputs(argv):
    parsed_args = isort_parse_args(argv)
    assert isinstance(parsed_args, dict), "Expected a dictionary"
    assert len(parsed_args) > 0, "Expected non-empty dictionary"
