
import pytest
from thefuck.shells.generic import Generic

def test_get_builtin_commands():
    generic = Generic()
    commands = generic.get_builtin_commands()
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
    assert commands == expected_commands, f"Expected {expected_commands}, but got {commands}"
