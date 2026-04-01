
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree

def test_edge_cases():
    # Create a temporary directory for testing
    src = Path("test_src")
    dst = Path("test_dst")
    
    # Test case 1: Source and destination are the same (should not raise an error)
    copy_tree(src, src)
    
    # Test case 2: Destination does not exist, should create it
    copy_tree(src, dst)
    
    # Test case 3: Overwrite existing files in destination
    os.makedirs(dst / "subdir")
    (src / "file1").touch()
    shutil.copy2(src / "file1", dst / "file1")
    copy_tree(src, dst, overwrite=True)
    
    # Test case 4: Do not overwrite existing files in destination
    (dst / "newfile").touch()
    copy_tree(src, dst)
