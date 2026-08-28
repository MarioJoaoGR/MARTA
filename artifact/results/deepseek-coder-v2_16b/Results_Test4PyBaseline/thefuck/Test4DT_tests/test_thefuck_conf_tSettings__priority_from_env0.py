# Module: thefuck.conf
import pytest
from thefuck.conf import Settings

# Test cases for _priority_from_env method in Settings class

@pytest.fixture
def settings():
    return Settings()

# Basic usage test case
def test_basic_usage(settings):
    val = "rule1=10:rule2=20"
    result = list(settings._priority_from_env(val))
    assert result == [('rule1', 10), ('rule2', 20)]

# Invalid input handling test case
def test_invalid_input_handling(settings):
    val = "invalid:input:rule3=30"
    result = list(settings._priority_from_env(val))
    assert result == [('rule3', 30)]

# Empty input test case
def test_empty_input(settings):
    val = ""
    result = list(settings._priority_from_env(val))
    assert result == []

# Mixed content test case
def test_mixed_content(settings):
    val = "ruleA=50:invalidpair:ruleB=60"
    result = list(settings._priority_from_env(val))
    assert result == [('ruleA', 50), ('ruleB', 60)]

# Single pair test case
def test_single_pair(settings):
    val = "singleRule=1"
    result = list(settings._priority_from_env(val))
    assert result == [('singleRule', 1)]
