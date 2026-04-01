
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree

def test_valid_inputs():
    # Create a temporary directory for testing
    src = Path("test_src")
    dst = Path("test_dst")
    
    # Ensure the destination directory does not exist initially
    if dst.exists():
        shutil.rmtree(dst)
    
    # Create source directory and files
    os.makedirs(src, exist_ok=True)
    (src / "file1").touch()
    (src / "dir1").mkdir()
    (src / "dir1" / "file2").touch()
    
    # Call the function to copy the tree
    copy_tree(src, dst)
    
    # Check if the destination directory and files are created
    assert dst.is_dir(), "Destination directory was not created."
    assert (dst / "file1").exists(), "File 'file1' was not copied to the destination."
    assert (dst / "dir1").is_dir(), "Directory 'dir1' was not copied to the destination."
    assert (dst / "dir1" / "file2").exists(), "File 'file2' was not copied to the destination directory."
    
    # Clean up temporary files and directories
    shutil.rmtree(src)
    shutil.rmtree(dst)
