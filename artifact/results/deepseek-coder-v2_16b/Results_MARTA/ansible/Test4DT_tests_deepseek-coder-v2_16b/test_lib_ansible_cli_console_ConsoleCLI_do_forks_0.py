
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def valid_forks():
    return ConsoleCLI(args={'forks': '4'})

@pytest.fixture
def invalid_forks():
    return ConsoleCLI(args={'forks': '-1'})

@pytest.fixture
def no_forks():
    with pytest.raises(ValueError):
        return ConsoleCLI(args={})



def test_missing_forks():
    with pytest.raises(ValueError) as e:
        ConsoleCLI(args={})
    assert str(e.value) == 'A non-empty list for args is required'