
import pytest
from ansible.plugins.lookup.nested import LookupModule

@pytest.fixture(scope="module")
def lookup_module():
    return LookupModule()


def test_invalid_input(lookup_module):
    terms = []
    with pytest.raises(Exception):
        lookup_module.run(terms)