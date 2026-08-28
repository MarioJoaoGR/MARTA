
import pytest
from pysnooper.utils import shitcode


def test_ascii_only():
    assert shitcode("1234567890abcdef") == "1234567890abcdef"
