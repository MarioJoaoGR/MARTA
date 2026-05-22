
import pytest
from httpie.context import Environment

@pytest.fixture(scope="module")
def env():
    return Environment()

# Now we can use the 'env' fixture in our test case
def test_valid_input(env):
    assert isinstance(env, Environment)
