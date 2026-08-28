
import pytest
from mimesis.random import Random
import uuid
import string
import secrets

@pytest.fixture
def random_instance():
    return Random()

def test_randstr_default_length(random_instance):
    result = random_instance.randstr()
    assert isinstance(result, str)
    assert len(result) >= 16 and len(result) <= 128

def test_randstr_specific_length(random_instance):
    length = 32
    result = random_instance.randstr(length=length)
    assert isinstance(result, str)
    assert len(result) == length

def test_randstr_unique(random_instance):
    unique_string1 = random_instance.randstr(unique=True)
    unique_string2 = random_instance.randstr(unique=True)
    assert isinstance(unique_string1, str)
    assert isinstance(unique_string2, str)
    assert unique_string1 != unique_string2
