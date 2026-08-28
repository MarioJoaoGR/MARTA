
import pytest
from pypara.currencies import Currencies, Currency
from typing import Set

# Assuming Currencies and Currency are defined in a module named 'pypara.dcc'
# from pypara.dcc import Currencies, Currency

def _as_ccys(codes: Set[str]) -> Set[Currency]:
    """
    Converts a set of currency codes to a set of currencies.
    """
    return {Currencies[c] for c in codes}

# Test cases
def test_valid_case():
    # Define a set of valid currency codes
    codes = {"USD", "EUR"}
    
    # Convert the set of currency codes to a set of Currency objects
    ccys = _as_ccys(codes)
    
    # Assert that the result is a set containing Currency objects for USD and EUR
    assert len(ccys) == 2
    assert any(isinstance(c, Currency) and c.code == "USD" for c in ccys)
    assert any(isinstance(c, Currency) and c.code == "EUR" for c in ccys)
