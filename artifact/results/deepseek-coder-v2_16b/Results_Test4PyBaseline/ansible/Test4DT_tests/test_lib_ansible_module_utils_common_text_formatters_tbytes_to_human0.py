# Module: ansible.module_utils.common.text.formatters
import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

# Define the size ranges for conversion
SIZE_RANGES = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 * 1024,
    'GB': 1024 * 1024 * 1024,
    'TB': 1024 * 1024 * 1024 * 1024,
    # Add more if needed
}

def iteritems(d):
    return [(k, v) for k, v in d.items()]

# Test cases
@pytest.mark.parametrize("size, isbits, unit, expected", [
    (1024, False, None, '1.00 KB'),  # Default conversion from bytes to kilobytes
    (1024, True, None, '8.00 Kb'),   # Conversion from bits to kilobits
    (1500, None, 'B', '1.46 KB'),    # Specific unit conversion to kilobytes
    (1500, True, 'K', '12.21 Kb'),   # Mixed unit and bit conversion
    (2500000, None, 'MB', '2.34 MB'),# Conversion from bytes to megabytes
])
def test_bytes_to_human(size, isbits, unit, expected):
    assert bytes_to_human(size, isbits, unit) == expected
