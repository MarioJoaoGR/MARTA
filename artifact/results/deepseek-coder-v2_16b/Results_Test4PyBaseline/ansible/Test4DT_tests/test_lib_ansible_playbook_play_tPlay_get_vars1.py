
import pytest
from ansible.playbook.play import Play

@pytest.fixture
def play():
    # Create an instance of the Play class for testing
    return Play()

# Test case to check if getting variables returns a copy
def test_get_vars(play):
    play.vars = {'var1': 'value1', 'var2': 'value2'}
    vars_copy = play.get_vars()
    assert play.vars == vars_copy, "Getting variables should return a copy"