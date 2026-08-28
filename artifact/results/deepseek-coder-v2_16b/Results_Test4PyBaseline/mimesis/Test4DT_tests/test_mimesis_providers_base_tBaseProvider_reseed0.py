
import pytest
from mimesis import BaseProvider
import random
from unittest.mock import patch, MagicMock
import enum

# Test initialization with a specific seed
def test_baseprovider_init_with_specific_seed():
    provider = BaseProvider(seed=12345)
    assert provider.seed == 12345

# Test reseeding without changing the seed value
def test_baseprovider_reseed_without_changing_seed():
    provider = BaseProvider(seed=12345)
    initial_seed = provider.seed
    provider.reseed()