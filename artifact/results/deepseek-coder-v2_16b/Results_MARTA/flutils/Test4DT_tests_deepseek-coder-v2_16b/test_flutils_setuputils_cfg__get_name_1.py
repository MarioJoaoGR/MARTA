
import pytest
from configparser import ConfigParser
from flutils.setuputils.cfg import _get_name

# Test for a valid case where 'metadata' section contains 'name' option set to a non-empty string
def test_valid_case():
    parser = ConfigParser()
    parser['metadata'] = {'name': 'Test Name'}
    setup_cfg_path = 'test.cfg'
    parser.write(open(setup_cfg_path, 'w'))
    
    name = _get_name(parser, setup_cfg_path)
    assert name == 'Test Name'

# Test for handling missing metadata section in the config file
def test_missing_section_case():
    parser = ConfigParser()
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, 'test.cfg')
    assert "The config file, 'test.cfg', is missing the 'metadata' section." in str(excinfo.value)

# Test for handling missing name option within the metadata section
def test_missing_option_case():
    parser = ConfigParser()
    parser['metadata'] = {}
    setup_cfg_path = 'test.cfg'
    parser.write(open(setup_cfg_path, 'w'))
    
    with pytest.raises(LookupError) as excinfo:
        _get_name(parser, setup_cfg_path)
    assert "The 'metadata', section is missing the 'name' option in the config file, 'test.cfg'." in str(excinfo.value)
