
import pytest
from httpie.context import Environment
import sys
import io
import platform

def print_debug_info(env: Environment):
    env.stderr.writelines([
        f'HTTPie {httpie_version}\n',
        f'Requests {requests_version}\n',
        f'Pygments {pygments_version}\n',
        f'Python {sys.version}\n{sys.executable}\n',
        f'{platform.system()} {platform.release()}',
    ])
    env.stderr.write('\n\n')
    env.stderr.write(repr(env))
    env.stderr.write('\n')

# Test default initialization
def test_default_initialization():
    env = Environment()
    assert hasattr(env, 'is_windows'), "Environment should have an attribute is_windows"
    assert isinstance(env.is_windows, bool), "Attribute is_windows should be a boolean"

# Test custom configuration with devnull

# Test error handling with invalid environment