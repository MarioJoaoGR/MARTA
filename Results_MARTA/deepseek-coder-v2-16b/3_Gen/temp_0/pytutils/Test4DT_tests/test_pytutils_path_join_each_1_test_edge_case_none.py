
import pytest
import os
from unittest.mock import patch

def join_each(parent, iterable):
    for p in iterable:
        yield os.path.join(parent, p)

@pytest.mark.parametrize("iterable", [(['child1', 'child2']), (['folder1', 'file1.txt'])])
def test_edge_case_none(iterable):
    with patch('os.path.join') as mock_join:
        parent = None
        join_each(parent, iterable)
        mock_join.assert_not_called()
