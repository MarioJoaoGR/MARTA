
import os
from pathlib import Path
import pytest
from flutils.pathutils import path_absent, normalize_path



def test_existing_file():
    existing_file = Path('test_file.txt')
    with open(existing_file, 'w') as f:
        f.write("Test content")
    assert os.path.exists(existing_file)
    path_absent(existing_file)
    assert not os.path.exists(existing_file)
