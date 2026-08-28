
import pytest
from py_backwards.conf import Settings

def test_default_debug_setting():
    settings = Settings()
    assert not settings.debug, "Default debug setting should be False"

def test_set_debug_to_true():
    settings = Settings()
    settings.debug = True
    assert settings.debug, "Setting debug to True should result in debug being True"

def test_set_debug_to_false():
    settings = Settings()
    settings.debug = False
    assert not settings.debug, "Setting debug to False should result in debug being False"
