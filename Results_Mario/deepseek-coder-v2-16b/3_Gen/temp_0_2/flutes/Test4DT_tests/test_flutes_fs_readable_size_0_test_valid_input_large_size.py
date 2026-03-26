
import pytest
from unittest.mock import patch
from flutes.fs import readable_size

@pytest.mark.parametrize("size, n_digits, expected", [
    (1024 * 1024, 2, "1.00M"),
    (500000, 2, "488.28K"),
    (123456789, 2, "117.74M")
])
@patch('flutes.fs.readable_size')
def test_valid_input_large_size(mock_readable_size, size, n_digits, expected):
    mock_readable_size.return_value = expected
    assert readable_size(size, n_digits) == expected
