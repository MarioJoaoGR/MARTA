# Module: pypara.monetary
# Import the function from the module
from pypara.monetary import NonePrice

def test_NonePrice_gt():
    # Create an instance of NonePrice
    none_price = NonePrice()
    
    # Test comparison with another price (should always return False)
    assert not none_price.gt(NonePrice())  # Ensure the other price is also a NonePrice instance

