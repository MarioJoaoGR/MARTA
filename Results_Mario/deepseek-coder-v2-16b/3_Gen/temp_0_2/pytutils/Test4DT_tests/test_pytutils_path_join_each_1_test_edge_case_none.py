
import os
import pytest
from pytutils.path import join_each

def test_edge_case_none():
    directory_path = None
    file_names = ['file1.txt', 'file2.txt']
    
    with pytest.raises(TypeError):
        for _ in join_each(directory_path, file_names):
            pass
