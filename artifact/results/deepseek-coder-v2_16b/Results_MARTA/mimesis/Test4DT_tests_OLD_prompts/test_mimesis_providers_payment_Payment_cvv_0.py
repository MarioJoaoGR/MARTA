
import pytest
from mimesis.providers.payment import Payment
from unittest.mock import patch


def test_edge_case_none():
    with pytest.raises(AttributeError):
        Payment().__person