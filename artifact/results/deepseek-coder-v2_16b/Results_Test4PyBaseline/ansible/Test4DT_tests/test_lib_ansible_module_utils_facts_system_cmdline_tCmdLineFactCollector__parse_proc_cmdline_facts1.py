
import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
import shlex

# Fixture to create an instance of the class for testing
@pytest.fixture
def collector():
    return CmdLineFactCollector()

# Test case for parsing command line arguments with multiple instances of the same argument
def test_parse_cmdline_facts_multiple_instances(collector):
    data = 'arg1=value1 arg2=value2 arg1=value3'
    result = collector._parse_proc_cmdline_facts(data)
    assert result == {'arg1': ['value1', 'value3'], 'arg2': 'value2'}

# Test case for parsing command line arguments with a single instance of an argument
def test_parse_cmdline_facts_single_instance(collector):
    data = 'arg1 arg2=value2 arg1'
    result = collector._parse_proc_cmdline_facts(data)
    assert result == {'arg1': True, 'arg2': 'value2'}

# Test case for parsing command line arguments with invalid input (should not raise an error)
def test_parse_cmdline_facts_invalid_input(collector):
    data = 'invalid input'
    result = collector._parse_proc_cmdline_facts(data)