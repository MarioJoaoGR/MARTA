
import pytest
from mimesis.providers.payment import Payment
from mimesis.enums import Gender

def test_credit_card_owner_default():
    payment_instance = Payment()
    owner_info = payment_instance.credit_card_owner()
    assert 'credit_card' in owner_info
    assert 'expiration_date' in owner_info
    assert 'owner' in owner_info
    assert isinstance(owner_info['credit_card'], str)
    assert isinstance(owner_info['expiration_date'], str)
    assert isinstance(owner_info['owner'], str)

