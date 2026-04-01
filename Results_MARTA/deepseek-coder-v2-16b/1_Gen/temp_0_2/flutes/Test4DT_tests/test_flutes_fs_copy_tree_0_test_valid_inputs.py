
import os
import shutil
from pathlib import Path
from flutes.fs import copy_tree

def test_valid_inputs():
    src = Path('source_dir')
    dst = Path('destination_dir')
    
    # Create a temporary source directory with some files and subdirectories
    os.makedirs(src, exist_ok=True)
    (src / 'file1').touch()
    (src / 'subdir').mkdir()
    (src / 'subdir' / 'file2').touch()
    
    # Ensure the destination directory does not exist initially
    if dst.exists():
        shutil.rmtree(dst)
    
    # Call the function to copy the tree
    copy_tree(src, dst)
    
    # Check that the destination directory was created and contains the copied files
    assert dst.is_dir()
    assert (dst / 'file1').exists()
    assert (dst / 'subdir' / 'file2').exists()
    
    # Clean up temporary directories and files
    shutil.rmtree(src)
    if dst.exists():
        shutil.rmtree(dst)
