
import pytest
from unittest.mock import patch, MagicMock
from configparser import ConfigParser
from ansible.config.manager import get_ini_config_value

def test_get_ini_config_value_with_valid_section_and_key():
    p = ConfigParser()
    p['server'] = {'port': '8080'}
    entry = {'section': 'server', 'key': 'port'}
    expected = '8080'
    
    with patch('configparser.ConfigParser') as mock_config:
        mock_section = MagicMock()
        mock_section['port'] = '8080'
        mock_config.return_value.__getitem__.return_value = mock_section
        
        assert get_ini_config_value(p, entry) == expected


def test_get_ini_config_value_with_nonexistent_section():
    p = ConfigParser()
    p['server'] = {'port': '8080'}
    entry = {'section': 'nonexistent', 'key': 'nonexistent'}
    expected = None
    
    with patch('configparser.ConfigParser') as mock_config:
        mock_config.return_value.__getitem__.side_effect = KeyError
        
        assert get_ini_config_value(p, entry) == expected