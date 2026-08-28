
import pytest
from ansible.cli.adhoc import AdHocCLI

@pytest.fixture(scope="module")
def adhoc_cli():
    return AdHocCLI()

@pytest.fixture(autouse=True)
def setup_parser(adhoc_cli):
    adhoc_cli.init_parser()
    return adhoc_cli

# Test Scenario 1: test_valid_inputs
def test_valid_inputs(adhoc_cli):
    args = ['specific_hosts', '-m', 'shell', '-a', 'cmd=echo hello']
    parsed_args = adhoc_cli.parser.parse_args(args)
    assert parsed_args.module_name == 'shell'
    assert parsed_args.module_args == 'cmd=echo hello'
    assert parsed_args.args == 'specific_hosts'

# Test Scenario 2: test_edge_cases
def test_edge_cases(adhoc_cli):
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args([None])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args([])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['', 'specific_hosts'])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['specific_hosts', '-m', None, '-a', 'cmd=echo hello'])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['specific_hosts', '-m', '', '-a', 'cmd=echo hello'])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['specific_hosts', '-m', 'shell', '-a', None])
    
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['specific_hosts', '-m', 'shell', '-a', ''])

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs(adhoc_cli):
    with pytest.raises(SystemExit):
        adhoc_cli.parser.parse_args(['invalid_host', '-m', 'invalid_module', '-a', 'invalid_arg=value'])
