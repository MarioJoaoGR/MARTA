
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        formatter = __StringFormatter(12345)
    assert "Expected \"str\", received \"int\"" in str(exc_info.value)
