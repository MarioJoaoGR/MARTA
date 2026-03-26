
import os
import pytest
from unittest.mock import patch

def join_each(parent, iterable):
    for p in iterable:
        yield os.path.join(parent, p)

@pytest.mark.parametrize("parent, iterable", [
    (None, ['file1', 'file2']),
    ('/home/user', None),
    (None, None)
])
def test_edge_case_none(parent, iterable):
    with pytest.raises(TypeError):
        list(join_each(parent, iterable))
