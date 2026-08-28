
# Module: mimesis.providers.internet
# test_internet.py
from mimesis import Internet
import pytest
from ipaddress import IPv6Address

@pytest.fixture
def internet():
    return Internet()

def test_default_initialization(internet):
    assert isinstance(internet, Internet)
    assert hasattr(internet, 'random')
    assert hasattr(internet, '_MAX_IPV4')
    assert hasattr(internet, '_MAX_IPV6')
    assert internet._MAX_IPV4 == (2 ** 32) - 1
    assert internet._MAX_IPV6 == (2 ** 128) - 1

def test_initialization_with_specific_seed(internet):
    specific_seed = 12345
    internet_with_seed = Internet(seed=specific_seed)
    assert isinstance(internet_with_seed, Internet)
    assert hasattr(internet_with_seed, 'random')
    assert hasattr(internet_with_seed, '_MAX_IPV4')
    assert hasattr(internet_with_seed, '_MAX_IPV6')
    assert internet_with_seed._MAX_IPV4 == (2 ** 32) - 1