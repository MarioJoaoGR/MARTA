
import pytest
from pypara.monetary import SomeMoney


def test_invalid_input():
    # Setup: Attempt to create an invalid SomeMoney instance
    with pytest.raises(TypeError):
        money = SomeMoney()  # Missing required arguments
    
    # The above setup should raise a TypeError, which is the expected behavior