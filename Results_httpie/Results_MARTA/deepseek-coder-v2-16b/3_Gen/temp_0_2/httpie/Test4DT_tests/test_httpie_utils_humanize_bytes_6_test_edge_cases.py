
import pytest
from httpie.utils import humanize_bytes

def test_humanize_bytes():
    assert humanize_bytes(1) == '1 B'
    assert humanize_bytes(1024, precision=1) == '1.0 kB'
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'
