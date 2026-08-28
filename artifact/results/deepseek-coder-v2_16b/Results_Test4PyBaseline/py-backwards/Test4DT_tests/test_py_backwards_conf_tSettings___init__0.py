# Module: py_backwards.conf
import pytest
from py_backwards.conf import Settings

# Test 1: Check default value of debug attribute
def test_default_debug_value():
    settings = Settings()
    assert not settings.debug, "Default value of debug should be False"

# Test 2: Set debug mode to True and check the value
def test_set_debug_mode_to_true():
    settings = Settings()
    settings.debug = True
    assert settings.debug, "Debug mode should be set to True after explicit assignment"

# Test 3: Ensure setting debug mode back to False works
def test_set_debug_mode_to_false():
    settings = Settings()
    settings.debug = False
    assert not settings.debug, "Debug mode should be set to False when explicitly assigned False"
