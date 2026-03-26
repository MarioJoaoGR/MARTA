
import pytest
import os
from unittest.mock import patch

def join_each(parent, iterable):
    for p in iterable:
        yield os.path.join(parent, p)

@pytest.mark.parametrize("iterable", [(['child1', 'child2']), (['folder1', 'file1.txt'])])
def test_edge_case_none(iterable):
    with patch('os.path.join') as mock_join:
        mock_join.return_value = "mocked_joined_path"
        parent = None
        result = list(join_each(parent, iterable))
        expected = ["mocked_joined_path"] * len(iterable)
        assert result == expected
