
# Module: mimesis.providers.generic
# test_generic.py
from mimesis import Generic
import pytest

@pytest.fixture
def generic_instance():
    return Generic(seed=12345)

def test_default_initialization(generic_instance):
    assert isinstance(generic_instance, Generic)
    assert hasattr(generic_instance, 'locale')
    assert hasattr(generic_instance, 'seed')