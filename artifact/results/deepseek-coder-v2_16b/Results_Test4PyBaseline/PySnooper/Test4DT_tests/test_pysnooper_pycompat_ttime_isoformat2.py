
import pytest
from datetime import time
import pysnooper.pycompat as pycompat

# Test cases for the time_isoformat function
def test_time_isoformat_default():
    t = time(12, 34, 56, 78910)
    assert pycompat.time_isoformat(t) == '12:34:56.078910'

def test_time_isoformat_explicit():
    t = time(12, 34, 56, 78910)