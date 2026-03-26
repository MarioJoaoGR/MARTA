
from datetime import timedelta, timezone

import pytest

from isort._vendored.tomli._re import cached_tz


def test_invalid_input():
    with pytest.raises(ValueError):
        # Invalid hour string (not an integer)
        cached_tz("24", "30", "+")
