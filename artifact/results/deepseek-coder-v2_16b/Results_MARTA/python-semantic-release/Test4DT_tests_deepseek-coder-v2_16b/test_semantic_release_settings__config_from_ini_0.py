
import configparser
import pytest
from semantic_release.settings import _config_from_ini


def test_empty_input():
    parser = configparser.ConfigParser()
    with pytest.raises(configparser.NoSectionError):
        _config_from_ini([])
