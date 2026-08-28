
import pytest
from pathlib import Path
import os
from flutils.pathutils import chown

def test_chown_existing_file():
    # Arrange
    file_path = 'test_file.txt'
    open(file_path, 'w').close()  # Create an empty file
    
    # Act
    chown(file_path)
    
    # Assert
    assert os.stat(file_path).st_uid == os.getuid()
    assert os.stat(file_path).st_gid == os.getgid()
    
    # Clean up
    os.remove(file_path)


