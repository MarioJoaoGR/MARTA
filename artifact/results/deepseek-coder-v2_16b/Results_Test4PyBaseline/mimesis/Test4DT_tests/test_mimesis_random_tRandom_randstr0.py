
# Module: mimesis.random
import pytest
import uuid
from typing import Optional
import string
import secrets

class Random:
    def randint(self, min_val: int, max_val: int) -> int:
        return min_val + (min_val + max_val) // 2
    
    def randstr(self, unique: bool = False, length: Optional[int] = None) -> str:
        if unique:
            return str(uuid.uuid4().hex)
        if length is None:
            length = self.randint(16, 128)
        _string = string.ascii_letters + string.digits
        _string = ''.join(secrets.choice(_string) for _ in range(length))
        return _string

# Fixture to provide an instance of the Random class for testing
@pytest.fixture
def random_instance():
    return Random()

# Test cases for randstr method
def test_randstr_default_unique_false(random_instance):
    # When unique is False and length is not provided, it should generate a string of default length (16 to 128)
    result = random_instance.randstr(unique=False)
    assert isinstance(result, str), "Expected a string"
    assert len(result) >= 16 and len(result) <= 128, "Length should be within the default range (16 to 128)"

def test_randstr_custom_length(random_instance):
    # When length is specified, it should generate a string of that length
    custom_length = random_instance.randint(16, 128)
    result = random_instance.randstr(unique=False, length=custom_length)
    assert isinstance(result, str), "Expected a string"
    assert len(result) == custom_length, f"Length should be exactly {custom_length}"

def test_randstr_unique_true(random_instance):
    # When unique is True, it should generate a unique UUID as a string
    result = random_instance.randstr(unique=True)
    assert isinstance(result, str), "Expected a string"
    assert len(result) == 32, "UUID length should be exactly 32 characters"
    # Adding this assertion to ensure that each call generates a different UUID
    first_call = result
    second_call = random_instance.randstr(unique=True)
    assert first_call != second_call, "Each call with unique=True should generate a different UUID"
