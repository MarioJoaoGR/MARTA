
import pytest
from pytutils.excs import ok

class TestOk:
    def test_ok(self):
        with pytest.raises(AssertionError):
            # The following line should raise AssertionError if the context manager works correctly
            with ok():
                assert False, "This should fail silently without raising an error"
