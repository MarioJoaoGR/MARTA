
import pytest
from mimesis.providers.payment import Payment

@pytest.fixture(scope="function")
def payment_instance():
    return Payment()

# Test generating a valid CVV (3-digit number)
def test_valid_cvv(payment_instance):
    cvv = payment_instance.cvv()
    assert isinstance(cvv, int), "CVV should be an integer"
    assert 100 <= cvv <= 999, "CVV should be a 3-digit number"

# Test edge cases for CVV generation
@pytest.mark.parametrize("seed", [12345, 98765])
def test_edge_cvv(payment_instance, seed):
    payment_instance = Payment(seed=seed)
    cvv = payment_instance.cvv()
    assert isinstance(cvv, int), "CVV should be an integer"
    assert 100 <= cvv <= 999, "CVV should be a 3-digit number"

# Test handling of invalid inputs (e.g., non-integer values)
def test_invalid_cvv(payment_instance):
    with pytest.raises(TypeError):
        payment_instance.cvv("not an integer")
