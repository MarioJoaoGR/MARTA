
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

@pytest.mark.parametrize("input_string", ["Hello123", "abc123xyz"])
def test_valid_input(input_string):
    lazy_regex = LazyRegex(args=('^[a-zA-Z0-9]+$',), kwargs={'flags': re.IGNORECASE})
    assert lazy_regex.findall(input_string) == ['Hello', '123'] or ['abc', '123']
