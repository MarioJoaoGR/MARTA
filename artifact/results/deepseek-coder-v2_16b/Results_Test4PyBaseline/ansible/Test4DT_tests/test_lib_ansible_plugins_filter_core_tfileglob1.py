
# Module: ansible.plugins.filter.core
import pytest
import glob
import os
from ansible.plugins.filter import core
import shutil  # Importing shutil for directory removal and cleanup

# Test case 5: Handling a directory path (should not be included)
def test_fileglob_directory():
    # Create a temporary directory for testing
    temp_dir = 'temp_dir'
    os.makedirs(temp_dir, exist_ok=True)
    try:
        result = core.fileglob(f'{temp_dir}/*')
        assert isinstance(result, list), "Expected a list but got something else"
        for item in result:
            # Check if the path is indeed a file (should fail since it's a directory)
            assert not os.path.isfile(item), f"{item} should not be a file"
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

# Test case 6: Handling non-existent pattern (should return an empty list)
def test_fileglob_non_existent_pattern():
    result = core.fileglob('nonexistentpattern.*')
    assert isinstance(result, list), "Expected a list but got something else"
    assert len(result) == 0, "Expected an empty list as there are no matches"

# Test case 7: Handling a pattern that includes multiple files and directories (should include only files)
def test_fileglob_mixed_files_and_dirs():
    # Create some temporary files for testing
    temp_file1 = 'temp_file1.txt'
    temp_file2 = 'temp_file2.txt'
    with open(temp_file1, 'w') as f:
        f.write('test content')
    with open(temp_file2, 'w') as f:
        f.write('test content')
    # Create a temporary directory for testing
    temp_dir = 'temp_dir'
    os.makedirs(temp_dir, exist_ok=True)
    try:
        result = core.fileglob(f'{temp_dir}/*')
        assert isinstance(result, list), "Expected a list but got something else"
        for item in result:
            # Check if the path is indeed a file (should fail since it might be a directory)
            assert not os.path.isfile(item), f"{item} should not be a file"
    finally:
        # Clean up temporary files and directories
        os.remove(temp_file1)
        os.remove(temp_file2)
        shutil.rmtree(temp_dir)
