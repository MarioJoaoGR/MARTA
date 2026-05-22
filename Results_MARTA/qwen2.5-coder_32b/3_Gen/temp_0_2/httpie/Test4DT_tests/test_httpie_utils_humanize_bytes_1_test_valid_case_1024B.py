
import pytest
from httpie.utils import humanize_bytes

def test_valid_case_1024B():
    assert humanize_bytes(1024) == '1.00 kB'
