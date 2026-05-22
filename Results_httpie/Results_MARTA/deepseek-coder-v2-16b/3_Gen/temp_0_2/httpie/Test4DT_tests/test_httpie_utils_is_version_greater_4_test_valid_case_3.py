
import pytest
from unittest.mock import patch
from httpie.utils import is_version_greater

@pytest.mark.parametrize("version_1, version_2, expected", [
    ("1.0", "0.9", True),
    ("1.1", "1.2", False),
    ("2.0.1", "2.0.0", True),
    ("1.0.beta", "1.0.1", False)
])
def test_is_version_greater(version_1, version_2, expected):
    assert is_version_greater(version_1, version_2) == expected
