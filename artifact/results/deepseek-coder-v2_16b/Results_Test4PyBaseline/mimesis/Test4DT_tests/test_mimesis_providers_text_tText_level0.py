
import pytest
from mimesis.providers.base import BaseProvider
from mimesis.exceptions import NonEnumerableError
import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Test initialization without seed
def test_base_provider_initialization_without_seed():
    provider = BaseProvider()
    assert isinstance(provider, BaseProvider)