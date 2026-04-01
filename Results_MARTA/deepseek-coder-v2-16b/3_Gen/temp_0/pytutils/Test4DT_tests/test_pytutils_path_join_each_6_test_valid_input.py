
import pytest
import os
from unittest.mock import patch

def join_each(parent, iterable):
    for p in iterable:
        yield os.path.join(parent, p)

@pytest.mark.parametrize("parent, iterable, expected", [
    ("parent_dir", ["child1", "child2"], ['parent_dir/child1', 'parent_dir/child2']),
    ("base_path", ["folder1", "file1.txt"], ['base_path/folder1', 'base_path/file1.txt'])
])
def test_valid_input(parent, iterable, expected):
    with patch('os.path.join') as mock_join:
        mock_join.side_effect = lambda x, y: f"{x}/{y}"
        result = list(join_each(parent, iterable))
        assert result == expected
