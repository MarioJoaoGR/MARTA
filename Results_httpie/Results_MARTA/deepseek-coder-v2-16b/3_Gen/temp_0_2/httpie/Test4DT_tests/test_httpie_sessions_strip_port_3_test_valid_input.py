
import pytest
from unittest.mock import patch

def strip_port(hostname: str) -> str:
    return hostname.split(':')[0]

@pytest.mark.parametrize("input_str, expected", [
    ("example.com", "example.com"),
    ("example.com:8080", "example.com"),
    ("localhost:3000", "localhost")
])
def test_valid_input(input_str, expected):
    assert strip_port(input_str) == expected
