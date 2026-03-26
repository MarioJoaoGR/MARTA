
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree

def test_valid_input():
    src = Path("test_source")
    dst = Path("test_destination")
    
    # Create source directory with some files and subdirectories
    os.makedirs(src / "subdir1")
    (src / "file1").touch()
    (src / "subdir1" / "file2").touch()
    
    # Run the function
    copy_tree(src, dst)
    
    # Check if destination directory was created
    assert os.path.isdir(dst)
    
    # Check if files and subdirectories were copied correctly
    assert (dst / "file1").exists()
    assert (dst / "subdir1" / "file2").exists()
    
    # Clean up
    shutil.rmtree(src)
    shutil.rmtree(dst)
