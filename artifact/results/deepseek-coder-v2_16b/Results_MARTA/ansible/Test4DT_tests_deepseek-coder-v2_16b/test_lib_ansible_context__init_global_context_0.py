
import pytest
from ansible.context import GlobalCLIArgs

# Test valid inputs scenario
def test_valid_inputs():
    cli_args = {
        'verbose': True,
        'output_format': 'json',
        'loglevel': 'debug'
    }
    _init_global_context(cli_args)
    assert isinstance(CLIARGS, GlobalCLIArgs)
    assert CLIARGS.verbose == cli_args['verbose']
    assert CLIARGS.output_format == cli_args['output_format']
    assert CLIARGS.loglevel == cli_args['loglevel']

# Test edge cases scenario
def test_edge_cases():
    with pytest.raises(TypeError):
        _init_global_context(None)
    
    with pytest.raises(ValueError):
        _init_global_context({})

# Test invalid inputs scenario
def test_invalid_inputs():
    cli_args = {
        'verbose': True,
        'output_format': 'json',
        'loglevel': 'debug',
        'invalid_option': 'invalid'  # An example of an invalid option
    }
    with pytest.raises(AttributeError):
        _init_global_context(cli_args)
