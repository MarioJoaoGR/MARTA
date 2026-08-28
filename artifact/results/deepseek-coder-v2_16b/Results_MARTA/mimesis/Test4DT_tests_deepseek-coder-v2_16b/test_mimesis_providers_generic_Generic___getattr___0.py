
import pytest
from mimesis.providers.generic import Generic


def test_valid_input_with_specific_seed():
    specific_seed = 42
    generic_instance = Generic(seed=specific_seed)
    assert hasattr(generic_instance, 'locale')
    assert hasattr(generic_instance, 'seed')
    assert generic_instance.seed == specific_seed