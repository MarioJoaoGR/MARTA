
import pytest
from flutils.pathutils import normalize_path
from pathlib import Path
import os

# Helper function to create a temporary directory for testing expanduser and expandvars
def create_temp_dir():
    temp_dir = Path(os.getcwd(), "temp_test_dir")
    if not temp_dir.exists():
        temp_dir.mkdir()
    return temp_dir

# Test cases for normalize_path function
@pytest.mark.parametrize("input_path, expected", [
    ("~/tmp/foo/../bar", Path('/home/test_user/tmp/bar')),
    (Path("~/tmp/foo/../bar"), Path('/home/test_user/tmp/bar')),
    (b"~/tmp/foo/../bar", Path('/home/test_user/tmp/bar')),
    ("tmp/foo/../bar", Path(os.getcwd(), "tmp/bar")),
    ("~/env_var_test/../bar", Path('/home/test_user/env_var_test/../bar' if 'env_var_test' in os.environ else '/home/test_user/env_var_test/../bar')),
])
def test_normalize_path(input_path, expected):
    normalized_path = normalize_path(input_path)
    assert isinstance(normalized_path, Path), f"Expected {expected} but got {normalized_path}"