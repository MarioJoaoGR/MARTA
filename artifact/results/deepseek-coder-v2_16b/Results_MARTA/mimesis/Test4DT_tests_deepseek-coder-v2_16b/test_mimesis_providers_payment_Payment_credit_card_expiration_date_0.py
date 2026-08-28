
import pytest
from mimesis.providers.payment import Payment

def test_valid_input():
    payment_instance = Payment()
    minimum_year = 16
    maximum_year = 25
    expiration_date = payment_instance.credit_card_expiration_date(minimum=minimum_year, maximum=maximum_year)
    month, year = map(int, expiration_date.split('/'))
    assert minimum_year <= year <= maximum_year
