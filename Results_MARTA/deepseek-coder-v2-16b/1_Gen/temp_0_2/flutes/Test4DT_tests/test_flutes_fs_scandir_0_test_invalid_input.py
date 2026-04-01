
import pytest
from pathlib import Path
import os
from unittest.mock import patch

def scandir(path):
    """Lazily iterate over all files and directories under a directory."""
    if isinstance(path, Path):
        with os.scandir(path) as it:
            for entry in it:
                yield Path(entry.path)
    else:
        with os.scandir(path) as it:
            for entry in it:
                yield entry.path

@pytest.mark.parametrize("invalid_path", ["/nonexistent/directory", str(Path.home()) + "/nonexistent"])
def test_invalid_input(invalid_path):
    with patch('os.scandir', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            list(scandir(invalid_path))
