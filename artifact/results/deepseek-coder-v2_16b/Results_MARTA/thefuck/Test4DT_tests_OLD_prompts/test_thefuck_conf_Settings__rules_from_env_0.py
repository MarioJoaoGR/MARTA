
import pytest
from unittest.mock import patch
from thefuck.conf import Settings
import thefuck.const as const



def test_empty_rules():
    settings = Settings()
    with patch('thefuck.conf.Settings._rules_from_env', return_value=['DEFAULT_RULES']):
        result = settings._rules_from_env('')
        assert result == ['DEFAULT_RULES']