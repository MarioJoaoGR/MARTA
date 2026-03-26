
import pytest
from pytutils.excs import ok

class TestOk:
    def test_ok(self):
        with pytest.raises(ValueError):
            with ok(TypeError):
                int('abc')  # This will raise ValueError, not TypeError
