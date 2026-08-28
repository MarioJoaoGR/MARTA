
import pytest
from pathlib import Path
from flutils.pathutils import chmod

def test_valid_input_single_file():
    # Setup: Create a temporary file with specific permissions
    temp_file = Path('~/tmp/flutils.tests.osutils.txt').expanduser()
    temp_file.parent.mkdir(parents=True, exist_ok=True)
    temp_file.touch()
    chmod(temp_file, mode_file=0o660)
    
    # Assert that the file has the expected permissions
    assert (temp_file.stat().st_mode & 0o777) == 0o660

