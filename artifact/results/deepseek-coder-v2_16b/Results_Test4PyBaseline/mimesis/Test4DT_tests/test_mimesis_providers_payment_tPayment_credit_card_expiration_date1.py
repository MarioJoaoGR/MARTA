
import pytest
from mimesis.providers.payment import Payment

# Test initialization with default settings
def test_default_initialization():
    payment = Payment()
    assert isinstance(payment, Payment), "Initialization should create a Payment instance"

# Test credit card expiration date generation
@pytest.mark.parametrize("minimum, maximum", [(16, 25)])
def test_credit_card_expiration_date(minimum, maximum):
    payment = Payment()
    expiration_date = payment.credit_card_expiration_date(minimum=minimum, maximum=maximum)
    
    # Split the generated date string to check month and year separately
    parts = expiration_date.split('/')
    assert len(parts) == 2, "Expiration date should be in 'MM/YY' format"
    
    month = int(parts[0])
    year = int(parts[1])
    
    # Check if the month is within the valid range (1 to 12)
    assert 1 <= month <= 12, "Month should be between 1 and 12"
    
    # Check if the year is within the specified range (minimum to maximum)
    assert minimum <= year <= maximum, f"Year should be between {minimum} and {maximum}"
