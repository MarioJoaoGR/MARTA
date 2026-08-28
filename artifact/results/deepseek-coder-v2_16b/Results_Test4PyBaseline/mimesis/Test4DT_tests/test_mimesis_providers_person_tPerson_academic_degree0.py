
import pytest
from mimesis.providers.person import Person

# Test initialization with a specific seed
def test_init_with_seed():
    provider = Person(seed=12345)
    assert provider.seed == 12345

# Test initialization without providing a seed (uses current system time)
def test_init_without_seed():
    provider = Person()
    # Since the exact moment of initialization can vary, we check that it's not None or equal to the default value.
    assert provider.seed is not None and provider.seed != 0

# Test reseeding with a specific seed
def test_reseed_with_specific_seed():
    provider = Person()
    initial_seed = provider.seed
    provider.reseed(seed=67890)
    assert provider.seed == 67890
    # Optionally, you can check that the seed has changed from the initial one
    assert provider.seed != initial_seed

# Test reseeding without providing a seed (uses current system time)
def test_reseed_without_specific_seed():
    provider = Person()
    initial_seed = provider.seed
    provider.reseed()
    # Since the exact moment of reseeding can vary, we check that it's not equal to the previous seed.