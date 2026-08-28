
import pytest
from pypara.monetary import SomeMoney

# Test cases for the `is_equal` method of the SomeMoney class
def test_is_equal_same_instance():
    money1 = SomeMoney(ccy="USD", qty=100, dov=None)  # Corrected to include required arguments
    assert money1.is_equal(money1) == True

def test_is_equal_different_instances():
    money1 = SomeMoney(ccy="USD", qty=100, dov=None)
    money2 = SomeMoney(ccy="USD", qty=100, dov=None)
    assert money1.is_equal(money2) == True

def test_is_equal_different_classes():
    class DifferentMoney:
        pass
    
    different_money = DifferentMoney()
    money1 = SomeMoney(ccy="USD", qty=100, dov=None)
    assert money1.is_equal(different_money) == False

def test_is_equal_different_values():
    money1 = SomeMoney(ccy="USD", qty=100, dov=None)
    money2 = SomeMoney(ccy="USD", qty=200, dov=None)
    assert money1.is_equal(money2) == False
