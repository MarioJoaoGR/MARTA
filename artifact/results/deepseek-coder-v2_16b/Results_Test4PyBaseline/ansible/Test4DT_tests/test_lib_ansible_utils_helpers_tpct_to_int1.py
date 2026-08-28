
import pytest
from ansible.utils.helpers import pct_to_int

# Test cases for converting percentage to integer
def test_pct_to_int_percentage():
    assert pct_to_int("50%", 200) == 100