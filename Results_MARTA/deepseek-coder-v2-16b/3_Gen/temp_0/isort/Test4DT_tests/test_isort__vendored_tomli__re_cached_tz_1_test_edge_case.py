
from datetime import timedelta, timezone

import pytest

from isort._vendored.tomli._re import cached_tz


def test_edge_case():
    # Test edge case where hour and minute are at their extreme values
    with pytest.raises(ValueError):
        # Invalid hour value (should be between 0 and 23)
        cached_tz("24", "00", "+")
