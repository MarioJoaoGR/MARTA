
import os
import shutil
from pathlib import Path
import contextlib
import pytest

# Import the function from its module
from flutes.fs import copy_tree

@pytest.fixture
def setup_test_dirs():
    # Create a temporary source directory with some files and subdirectories
    src = Path('test_src')
    dst = Path('test_dst')
    
    os.makedirs(src, exist_ok=True)
    (src / 'file1').touch()
    (src / 'subdir').mkdir()
    (src / 'subdir' / 'file2').touch()
    
    yield src, dst
    
    # Clean up after the test
    shutil.rmtree(src)
    if os.path.exists(dst):
        shutil.rmtree(dst)

def test_copy_tree_without_overwrite(setup_test_dirs):
    src, dst = setup_test_dirs
    
    # Call the function to copy contents from source to destination without overwriting existing files
    copy_tree(src, dst)
    
    # Check if all files and subdirectories are copied correctly
    assert (dst / 'file1').exists(), "The file should be copied"
    assert (dst / 'subdir' / 'file2').exists(), "The subdirectory should be copied"