
import pytest
from unittest.mock import MagicMock, patch
from pypara.accounting.ledger import LedgerEntry, Quantity



def test_error_case():
    with pytest.raises(TypeError):
        ledger = MagicMock()
        posting = MagicMock()  # No is_debit attribute set
        balance = Quantity(value=100)
        LedgerEntry(ledger=ledger, posting=posting, balance=balance)