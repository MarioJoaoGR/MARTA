
import pytest
from datetime import time
import pysnooper.pycompat as pycompat

def test_valid_time():
    t = time(12, 34, 56, 7890)
    result = pycompat.time_isoformat(t)
    assert result == '12:34:56.007890'

