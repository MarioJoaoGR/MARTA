
import pytest
from pypara.accounting.ledger import LedgerEntry, Posting, Quantity

# Test for valid input initialization of LedgerEntry

# Test for LedgerEntry initialization without a journal
def test_missing_journal():
    with pytest.raises(TypeError):
        LedgerEntry(ledger="someLedgerInstance", posting=Posting(), balance=Quantity())