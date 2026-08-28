
import pytest
from mimesis import BaseProvider
import random

# Fixture to provide a BaseProvider instance with a specific seed
@pytest.fixture
def base_provider():
    return BaseProvider(seed=12345)

# Test initialization of BaseProvider with a specific seed
def test_base_provider_initialization_with_specific_seed():
    provider = BaseProvider(seed=12345)
    assert provider.seed == 12345

# Test reseeding without changing the seed value
def test_reseeding_without_changing_the_seed(base_provider):
    initial_seed = base_provider.seed
    base_provider.reseed()