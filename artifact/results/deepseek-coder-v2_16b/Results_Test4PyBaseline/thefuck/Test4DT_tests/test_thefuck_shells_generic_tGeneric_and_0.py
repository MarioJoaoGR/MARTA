# Module: thefuck.shells.generic
import pytest
from thefuck.shells.generic import Generic

# Create an instance of Generic
generic_instance = Generic()

@pytest.mark.parametrize("commands, expected", [
    (('echo "Hello"',), 'echo "Hello"'),
    (('echo "Hello"', 'ls -l'), 'echo "Hello" && ls -l'),
    (('echo "Hello"', 'ls -l', 'pwd'), 'echo "Hello" && ls -l && pwd')
])
def test_and_(commands, expected):
    assert generic_instance.and_(*commands) == expected
