
import pytest
from pypara.monetary import SomePrice, Currency, Date

# Test scenario 1: Creating a SomePrice object with USD currency and quantity

# Test scenario 2: Creating a SomePrice object with EUR currency and different quantity

# Test scenario 3: Creating a SomePrice object with invalid date and expected error
def test_with_dov_invalid_date():
    with pytest.raises(TypeError):
        price = SomePrice(Currency('USD'), 100.50)
        price.with_dov(Date(2023, 1, 1))