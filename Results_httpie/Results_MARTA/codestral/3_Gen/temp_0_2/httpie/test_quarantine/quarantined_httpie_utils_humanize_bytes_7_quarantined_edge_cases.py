
import pytest
from humanize_bytes import humanize_bytes

def test_edge_cases():
    # Test None input
    assert humanize_bytes(None) == '0 B'
    
    # Test zero value
    assert humanize_bytes(0) == '0 B'
    
    # Test negative value
    assert humanize_bytes(-1024) == '-1.00 kB'
    
    # Test exact boundary values
    assert humanize_bytes(1 << 10, precision=0) == '1.0 kB'
    assert humanize_bytes(1 << 20) == '1.00 MB'
    assert humanize_bytes(1 << 30) == '1.00 GB'
    assert humanize_bytes(1 << 40) == '1.00 TB'
    assert humanize_bytes(1 << 50) == '1.00 PB'
    
    # Test large values
    assert humanize_bytes(1024 * 123456, precision=2) == '120.75 MB'
    assert humanize_bytes(1024 * 123456789, precision=1) == '117.7 MB'
    
    # Test exact multiples of units
    assert humanize_bytes(1 << 10 - 1) == '1023 B'
    assert humanize_bytes(1 << 20 - 1) == '1048575 B'
    assert humanize_bytes(1 << 30 - 1) == '1073741823 B'
    
    # Test precision values
    assert humanize_bytes(1024 * 123, precision=0) == '123 kB'
    assert humanize_bytes(1024 * 123456, precision=0) == '120 MB'
    
    # Test empty list (should not affect the function)
    assert humanize_bytes([]) == '0 B'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_humanize_bytes_7_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_utils_humanize_bytes_7_test_edge_cases.py:3:0: E0401: Unable to import 'humanize_bytes' (import-error)


"""