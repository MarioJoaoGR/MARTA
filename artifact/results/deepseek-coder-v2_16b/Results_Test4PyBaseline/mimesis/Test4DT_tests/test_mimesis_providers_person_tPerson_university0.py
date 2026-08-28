
import pytest
from mimesis.providers.person import Person

# Test initialization with a specific seed
def test_init_with_seed():
    person_with_seed = Person(seed=12345)
    assert person_with_seed.seed == 12345

# Test initialization without a seed, should use system time as seed
def test_init_without_seed():
    person_without_seed = Person()
    # Since the seed is based on the current system time, we cannot directly assert its value here.
    # Instead, we can check that it's not None or a default value.