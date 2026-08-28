
# Module: ansible.module_utils.facts.system.cmdline
import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
import shlex

# Fixture to create an instance of the CmdLineFactCollector class for testing
@pytest.fixture
def collector():
    return CmdLineFactCollector()

# Test case to check if _parse_proc_cmdline correctly handles data with no equal sign
def test_parse_proc_cmdline_no_equal_sign(collector):
    data = "arg1 arg2"
    parsed_cmdline = collector._parse_proc_cmdline(data)
    assert parsed_cmdline == {'arg1': True, 'arg2': True}

# Test case to check if _parse_proc_cmdline correctly handles invalid data (missing equal sign)
def test_parse_proc_cmdline_invalid_data_missing_equal(collector):
    data = "arg1value1 arg2 value3"  # Missing '=' between arg and value
    parsed_cmdline = collector._parse_proc_cmdline(data)
    assert parsed_cmdline == {'arg1value1': True, 'arg2': True, 'value3': True}

# Test case to check if _parse_proc_cmdline correctly handles multiple equal signs
def test_parse_proc_cmdline_multiple_equals(collector):
    data = "arg1=value1=extra arg2 value3"
    parsed_cmdline = collector._parse_proc_cmdline(data)
    assert parsed_cmdline == {'arg1': 'value1=extra', 'arg2': True, 'value3': True}

# Test case to check if _parse_proc_cmdline correctly handles empty data
def test_parse_proc_cmdline_empty_data(collector):
    data = ""
    parsed_cmdline = collector._parse_proc_cmdline(data)
    assert parsed_cmdline == {}

# Test case to check if _parse_proc_cmdline returns the correct dictionary format
def test_parse_proc_cmdline_return_type(collector):
    data = "arg1=value1 arg2 value3"
    parsed_cmdline = collector._parse_proc_cmdline(data)
    assert isinstance(parsed_cmdline, dict), f"Expected a dictionary but got {type(parsed_cmdline)}"
