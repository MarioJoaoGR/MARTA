
import pytest
from configparser import ConfigParser
import os
from flutils.setuputils.cfg import _get_name

# Test for valid configuration file
def test_valid_config():
    parser = ConfigParser()
    parser['metadata'] = {'name': 'test_name'}
    with open('setup.cfg', 'w') as cfgfile:
        parser.write(cfgfile)
    assert _get_name(parser, 'setup.cfg') == 'test_name'
    os.remove('setup.cfg')

# Test for missing section in configuration file
def test_missing_section():
    parser = ConfigParser()
    with pytest.raises(LookupError):
        _get_name(parser, 'setup.cfg')

# Test for missing option within the metadata section
def test_missing_option():
    parser = ConfigParser()
    parser['metadata'] = {}
    with open('setup.cfg', 'w') as cfgfile:
        parser.write(cfgfile)
    with pytest.raises(LookupError):
        _get_name(parser, 'setup.cfg')
    os.remove('setup.cfg')
