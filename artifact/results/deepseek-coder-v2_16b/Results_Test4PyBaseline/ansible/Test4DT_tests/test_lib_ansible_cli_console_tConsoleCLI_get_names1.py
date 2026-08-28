
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

# Test case for get_names method, focusing on line 122
def test_get_names(console):
    # Since get_names is a simple method that returns dir of self, we can assert it's not None or empty.
    names = console.get_names()
    assert names is not None
    assert len(names) > 0
