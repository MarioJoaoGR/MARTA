
import pytest
from mimesis import BaseProvider
import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Test initialization without seed
def test_base_provider_initialization_without_seed():
    provider = BaseProvider()
    assert isinstance(provider, BaseProvider)
    assert provider.seed is not None

# Test initialization with a specific seed
def test_base_provider_initialization_with_specific_seed():
    provider = BaseProvider(seed=12345)
    assert isinstance(provider, BaseProvider)
    assert provider.seed == 12345

# Test reseeding without changing the seed value
def test_base_provider_reseed():
    provider = BaseProvider(seed=12345)
    initial_seed = provider.seed
    provider.reseed()