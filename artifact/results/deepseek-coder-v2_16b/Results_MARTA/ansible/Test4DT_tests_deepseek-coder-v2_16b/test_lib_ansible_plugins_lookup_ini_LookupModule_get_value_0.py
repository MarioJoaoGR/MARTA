
import pytest
from io import StringIO
import configparser
import re
from ansible.plugins.lookup.ini import LookupModule

@pytest.fixture(scope="module")
def lookup_instance():
    instance = LookupModule()
    config = StringIO('[section]\nkey=value')
    instance.cp = configparser.ConfigParser()
    instance.cp.readfp(config)
    return instance

def test_valid_input_literal_string_key(lookup_instance):
    value = lookup_instance.get_value('key', 'section', dflt='default_value', is_regexp=False)
    assert value == 'value'

def test_valid_input_regexp_pattern(lookup_instance):
    pattern = re.compile(r'^k')
    values = lookup_instance.get_value(pattern, 'section', dflt='default_value', is_regexp=True)
    assert len(values) == 1 and values[0] == 'value'
