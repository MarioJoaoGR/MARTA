
import pytest
from lib.ansible.plugins.shell import ShellModule

# Test cases for the quote function
@pytest.fixture(params=[('no_spaces', '"no_spaces"'), 
                        (None, ''), 
                        (12345, '"12345"')])
def shell_module_instance(request):
    return ShellModule(), request.param[0]

@pytest.mark.parametrize("shell_module, input_value", [('no_spaces', 'hello world'), 
                                                       (None, None), 
                                                       (12345, 12345)])
def test_quote(shell_module, input_value):
    shell_instance = ShellModule()
    assert shell_instance.quote(input_value) == expected_output
