
import pytest
from unittest.mock import patch
from thefuck.conf import Settings

def test_priority_from_env_valid():
    settings = Settings()
    result = list(settings._priority_from_env('rule1=10:rule2=20'))
    assert len(result) == 2
    assert result[0] == ('rule1', 10)
    assert result[1] == ('rule2', 20)

def test_priority_from_env_invalid():
    settings = Settings()
    result = list(settings._priority_from_env('invalidinput'))
    assert len(result) == 0
