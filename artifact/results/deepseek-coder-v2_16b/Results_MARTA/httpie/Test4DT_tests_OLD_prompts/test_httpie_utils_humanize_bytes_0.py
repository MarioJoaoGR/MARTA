
import pytest
from unittest.mock import patch

def humanize_bytes(n, precision=2):
    abbrevs = [
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'B')
    ]

    if n == 1:
        return '1 B'

    for factor, suffix in abbrevs:
        if n >= factor:
            break

    return '%.*f %s' % (precision, n / factor, suffix)

@pytest.mark.parametrize("n, expected", [
    (1, '1 B'),
    (1024, '1.0 kB'),
    (1024 * 123, '123.0 kB'),
    (1024 * 12342, '12.1 MB'),
    (1024 * 12342, '12.05 MB'),
    (1024 * 1234, '1.21 MB'),
    (1024 * 1234 * 1111, '1.31 GB')
])
def test_valid_input_specified_precision(n, expected):
    assert humanize_bytes(n) == expected

@pytest.mark.parametrize("n, precision, expected", [
    (1024 * 123, 1, '123.0 kB'),
    (1024 * 12342, 2, '12.05 MB')
])
def test_valid_input_specified_precision(n, precision, expected):
    assert humanize_bytes(n, precision) == expected

@pytest.mark.parametrize("n", [None])
def test_invalid_input_none(n):
    with pytest.raises(TypeError):
        humanize_bytes(n)
