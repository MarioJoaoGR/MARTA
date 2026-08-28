# Module: thefuck.shells.generic
import pytest
from thefuck.shells.generic import Generic

# Test initialization of Generic instance
def test_generic_instance():
    generic_instance = Generic()
    assert isinstance(generic_instance, Generic)

# Test get_builtin_commands method
def test_get_builtin_commands():
    generic_instance = Generic()
    builtin_commands = generic_instance.get_builtin_commands()
    expected_commands = [
        'alias', 'bg', 'bind', 'break', 'builtin', 'case', 'cd',
        'command', 'compgen', 'complete', 'continue', 'declare',
        'dirs', 'disown', 'echo', 'enable', 'eval', 'exec', 'exit',
        'export', 'fc', 'fg', 'getopts', 'hash', 'help', 'history',
        'if', 'jobs', 'kill', 'let', 'local', 'logout', 'popd',
        'printf', 'pushd', 'pwd', 'read', 'readonly', 'return', 'set',
        'shift', 'shopt', 'source', 'suspend', 'test', 'times', 'trap',
        'type', 'typeset', 'ulimit', 'umask', 'unalias', 'unset',
        'until', 'wait', 'while'
    ]
    assert builtin_commands == expected_commands
