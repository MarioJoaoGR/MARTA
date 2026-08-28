
import pytest
from mimesis.providers.internet import Internet
from mimesis.exceptions import NonEnumerableError

def test_hashtags_default_quantity():
    internet = Internet()
    hashtags_list = internet.hashtags()
    assert isinstance(hashtags_list, list)
    assert len(hashtags_list) == 4

def test_hashtags_specified_quantity():
    internet = Internet()
    specified_quantity = 5
    hashtags_list = internet.hashtags(quantity=specified_quantity)
    assert isinstance(hashtags_list, list)
    assert len(hashtags_list) == specified_quantity
