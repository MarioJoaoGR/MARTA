
import os
import pickle
from unittest.mock import patch, MagicMock
import pytest

def wrapped(*args, **kwargs):
    if 'path' in kwargs:
        path = kwargs['path']
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file at path '{path}' does not exist.")
        with open(path, "rb") as f:
            ret = pickle.load(f)
    else:
        ret = kwargs['func']()
        if 'path' in kwargs and kwargs['path']:
            with open(kwargs['path'], "wb") as f:
                pickle.dump(ret, f)
    return ret

@pytest.mark.parametrize("invalid_path", ["nonexistentfile.pkl"])
def test_invalid_path(invalid_path):
    with pytest.raises(FileNotFoundError):
        wrapped(path=invalid_path)
