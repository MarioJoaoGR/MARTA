
import pytest
from unittest.mock import patch, MagicMock
import datetime
from pypara.dcc import _construct_date


def test_invalid_month():
    with pytest.raises(ValueError):
        _construct_date(2023, 13, 1)
