
import pytest
from unittest.mock import patch
from mimesis.providers.payment import Payment
from mimesis.providers.person import Person

def test_valid_input():
    with patch('mimesis.providers.payment.Payment.__init__', return_value=None):
        payment_instance = Payment()
        assert isinstance(payment_instance, Payment)

def test_edge_case():
    with patch('mimesis.providers.payment.Payment.__init__', return_value=None):
        payment_instance = Payment(seed=None)
        assert isinstance(payment_instance, Payment)
