
import pytest
from mimesis import BaseProvider
import random
import enum

# Fixture to provide a BaseProvider instance for testing
@pytest.fixture
def base_provider():
    return BaseProvider(seed=12345)

# Test case for initializing the BaseProvider with a specific seed
def test_init_with_specific_seed():
    provider = BaseProvider(seed=12345)
    assert provider.seed == 12345
    assert isinstance(provider.random, random.Random)

# Test case for reseeding without changing the seed value
def test_reseed_without_changing_seed(base_provider):
    initial_seed = base_provider.seed
    base_provider.reseed()