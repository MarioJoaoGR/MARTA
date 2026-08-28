
import pytest
from mimesis.providers.internet import Internet
from mimesis.exceptions import NonEnumerableError

@pytest.fixture(scope="module")
def internet_instance():
    return Internet()

def test_hashtags_default_quantity(internet_instance):
    hashtags = internet_instance.hashtags()
    assert isinstance(hashtags, list)
    assert len(hashtags) == 4

def test_hashtags_specific_quantity(internet_instance):
    hashtags = internet_instance.hashtags(quantity=3)
    assert isinstance(hashtags, list)
    assert len(hashtags) == 3
