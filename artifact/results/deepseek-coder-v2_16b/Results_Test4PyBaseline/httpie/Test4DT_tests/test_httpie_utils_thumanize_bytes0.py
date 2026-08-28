# Module: httpie.utils
import pytest
from httpie.utils import humanize_bytes

# Test cases for the humanize_bytes function
def test_humanize_bytes_default():
    assert humanize_bytes(1) == '1 B'

def test_humanize_bytes_with_precision():
    assert humanize_bytes(1024, precision=1) == '1.0 kB'

def test_humanize_bytes_large_number():
    assert humanize_bytes(1024 * 123, precision=1) == '123.0 kB'

def test_humanize_bytes_even_larger_number():
    assert humanize_bytes(1024 * 12342, precision=1) == '12.1 MB'

def test_humanize_bytes_very_large_number():
    assert humanize_bytes(1024 * 12342, precision=2) == '12.05 MB'

def test_humanize_bytes_extremely_large_number():
    assert humanize_bytes(1024 * 1234, precision=2) == '1.21 MB'

def test_humanize_bytes_extremely_large_number_higher_precision():
    assert humanize_bytes(1024 * 1234 * 1111, precision=2) == '1.31 GB'

def test_humanize_bytes_very_large_number_lower_precision():
    assert humanize_bytes(1024 * 1234 * 1111, precision=1) == '1.3 GB'
