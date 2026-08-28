
import pytest
from dataclasses import dataclass
from typing import List
from pypara.accounting.ledger import Ledger  # Assuming the module path is correct

# Define necessary classes for the test
@dataclass
class Account:
    name: str

@dataclass
class Balance:
    value: float

@dataclass
class LedgerEntry:
    balance: Balance

@dataclass
class Posting:
    amount: float
    direction: str  # 'debit' or 'credit'

@dataclass
class Quantity:
    value: float

# Test cases for the Ledger class and its methods
def test_ledger_initialization():
    ledger = Ledger(account=Account(name="Main"), initial=Balance(value=100.0))
    assert ledger.account.name == "Main"
    assert ledger.initial.value == 100.0