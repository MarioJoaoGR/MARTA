
# Module: pysnooper.pycompat
# test_pysnooper.py
from pysnooper.pycompat import PathLike
import pytest

class TestPathLike(PathLike):
    def __fspath__(self):
        raise NotImplementedError("NotImplementedError")

def test_pathlike():
    # Test that __fspath__ method raises NotImplementedError
    path_like = TestPathLike()
    with pytest.raises(NotImplementedError) as exc_info:
        path_like.__fspath__()
    assert str(exc_info.value) == "NotImplementedError"
