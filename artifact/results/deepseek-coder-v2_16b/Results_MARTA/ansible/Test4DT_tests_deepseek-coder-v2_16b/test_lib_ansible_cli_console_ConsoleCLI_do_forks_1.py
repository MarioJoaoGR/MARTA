
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def valid_forks():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*', 'forks': '4'})

@pytest.fixture
def invalid_forks():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*', 'forks': '-1'})

@pytest.fixture
def no_forks():
    return ConsoleCLI(args={})

def test_valid_forks(valid_forks):
    assert valid_forks.forks == 4

def test_invalid_forks(invalid_forks):
    with pytest.raises(ValueError) as e:
        invalid_forks.do_forks('-1')
    assert str(e.value) == 'forks must be greater than or equal to 1'

def test_missing_forks(no_forks):
    with pytest.raises(SystemExit):
        no_forks.onecmd('forks')
