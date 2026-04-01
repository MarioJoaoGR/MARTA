
import pytest
from flutes.fs import get_folder_size
from pathlib import Path
import subprocess

def test_valid_input():
    # Mocking the subprocess output for a known folder size
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(subprocess, 'check_output', lambda args, **kwargs: b'12345 /path/to/folder\n')
        
        # Test the function with a valid Path object
        folder_size = get_folder_size(Path('/path/to/folder'))
        assert folder_size == 12345
