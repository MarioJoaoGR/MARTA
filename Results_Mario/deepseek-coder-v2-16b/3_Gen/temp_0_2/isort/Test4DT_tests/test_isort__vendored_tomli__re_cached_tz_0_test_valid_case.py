
from datetime import timedelta, timezone
import pytest
from isort._vendored.tomli._re import cached_tz  # Correcting the import path

def test_valid_case():
    assert cached_tz("1", "30", "+") == timezone(timedelta(hours=1, minutes=30))
    assert cached_tz("2", "45", "-") == timezone(timedelta(hours=-2, minutes=-45))
    assert cached_tz("0", "0", "+") == timezone(timedelta(hours=0, minutes=0))
    assert cached_tz("1", "0", "+") == timezone(timedelta(hours=1, minutes=0))
    assert cached_tz("0", "15", "-") == timezone(timedelta(hours=-0, minutes=-15))
