
import pytest
from ansible.plugins.filter.core import to_datetime
import datetime

def test_valid_format():
    with pytest.raises(ValueError):
        to_datetime("invalid_date")
