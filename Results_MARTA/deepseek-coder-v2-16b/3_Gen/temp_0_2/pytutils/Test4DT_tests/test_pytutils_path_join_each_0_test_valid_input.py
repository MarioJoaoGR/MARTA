
import os
from pytutils.path import join_each

def test_valid_input():
    file_names = ['file1.txt', 'file2.txt']
    directory_path = '/home/user'
    
    expected_output = [os.path.join(directory_path, fn) for fn in file_names]
    
    result = list(join_each(directory_path, file_names))
    
    assert result == expected_output
