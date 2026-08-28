
import pytest
from ansible.config.manager import get_ini_config_value
import configparser

def test_get_ini_config_value_valid_input():
    p = configparser.ConfigParser()
    p['server'] = {'port': '8080'}
    entry = {'section': 'server', 'key': 'port'}
    assert get_ini_config_value(p, entry) == '8080'


def test_get_ini_config_value_nonexistent_section():
    p = configparser.ConfigParser()
    p['server'] = {'port': '8080'}
    entry = {'section': 'database', 'key': 'port'}
    assert get_ini_config_value(p, entry) is None

def test_get_ini_config_value_nonexistent_key():
    p = configparser.ConfigParser()
    p['server'] = {'port': '8080'}
    entry = {'section': 'server', 'key': 'host'}
    assert get_ini_config_value(p, entry) is None