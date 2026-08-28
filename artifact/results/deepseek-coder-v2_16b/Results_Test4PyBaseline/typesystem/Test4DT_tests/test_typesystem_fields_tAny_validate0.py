
import pytest
from typesystem.fields import Any

@pytest.fixture
def any_instance():
    return Any()

def test_validate_with_int(any_instance):
    result = any_instance.validate(123)
    assert result == 123

def test_validate_with_string(any_instance):
    result = any_instance.validate("test")