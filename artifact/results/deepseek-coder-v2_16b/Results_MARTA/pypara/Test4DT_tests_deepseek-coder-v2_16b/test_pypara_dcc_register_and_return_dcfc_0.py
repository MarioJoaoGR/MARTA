
import pytest
from pypara.dcc import DCC, DCCRegistry

# Define the DCFC type for clarity
DCFC = callable

def register_and_return_dcfc(func: DCFC) -> DCFC:
    """
    Registers the given day count fraction calculator and returns it.

    :param func: Day count fraction calculation function to be registered.
    :return: Registered day count fraction calculation function.
    """
    dcc = DCC(name="default", altnames=set(), ccys=set(), func=func)
    DCCRegistry.register(dcc)
    setattr(func, "__dcc", dcc)
    return func

# Test cases for register_and_return_dcfc function


def test_none_input():
    with pytest.raises(TypeError):
        register_and_return_dcfc(None)

def test_invalid_function():
    def invalid_func():
        pass
    
    with pytest.raises(TypeError):
        register_and_return_dcfc(invalid_func)