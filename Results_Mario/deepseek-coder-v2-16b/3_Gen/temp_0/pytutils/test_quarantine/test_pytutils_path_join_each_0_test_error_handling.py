
import os
from pytutils.path import join_each  # Assuming this module exists and has the function defined
import pytest
from unittest.mock import patch

def test_join_each():
    parent = 'parent_dir'
    iterable = ['child1', 'child2']
    
    with patch('os.path.join') as mock_join:
        # Set up the mock to return a specific value for testing
        expected_output = [f'{parent}/child1', f'{parent}/child2']
        mock_join.side_effect = lambda x, y: f"{x}/{y}"
        
        result = list(join_each(parent, iterable))
        
        # Assert that the mock was called with the expected arguments
        assert mock_join.call_count == len(iterable)
        for call in mock_join.mock_calls:
            assert call[1][0] == parent
            assert call[1][1] in iterable
        
        # Assert that the result matches the expected output
        assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""