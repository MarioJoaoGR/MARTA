
import os
import pytest
from flutils.pathutils import path_absent, normalize_path
from pathlib import Path

def test_path_absent_file():
    temp_file = 'temp_file.txt'
    with open(temp_file, 'w') as f:
        f.write('test content')
    
    assert os.path.exists(temp_file)
    
    path_absent(temp_file)
    
    assert not os.path.exists(temp_file)
