
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture(scope="module")
def cli():
    return ConsoleCLI(args={'host-pattern': 'app*.dc*'})


def test_invalid_case():
    with pytest.raises(TypeError):
        cli = ConsoleCLI()  # This should raise a TypeError because the constructor expects an argument