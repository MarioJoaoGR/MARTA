
# Module: pypara.accounting.ledger
# test_ledger_entry.py
import pytest
from datetime import date, datetime

# Assuming Ledger and Posting are defined elsewhere as per the examples provided
class Posting:
    def __init__(self, date: date):
        self.date = date

class Journal:
    def __init__(self):
        self.postings = []
    
    def add_posting(self, posting):
        self.postings.append(posting)

class Ledger:
    pass

class Quantity:
    pass

class LedgerEntry:
    """
    Provides a ledger entry model with methods to manage and retrieve information about the ledger entries.
    
    Attributes:
        ledger (Ledger[_T]): The ledger associated with this ledger entry.
        posting (Posting[_T]): The posting associated with this ledger entry.
        balance (Quantity): The balance of the ledger entry.
        
    Methods:
        date(): Returns the date of the ledger entry, which is derived from the posting's date.
    
    Example:
        To create a LedgerEntry instance, you would typically need to provide both a ledger and a posting. Here's an example:
        
        ```python
        from datetime import date
        class Posting:
            def __init__(self, date: date):
                self.date = date
        
        class Ledger:
            pass
        
        entry = LedgerEntry(ledger=Ledger(), posting=Posting(date=date.today()))  # Using today's date as an example.
        print(entry.date())  # This will print the posting's date, which is set when creating the Posting instance.
        ```
    
    The `date()` method in this class is designed to fetch and return the date associated with a ledger entry from its related posting. It does not require any parameters as it assumes that the necessary information (specifically, the 'posting' attribute) is already available within the same context or object instance. This method is crucial for financial systems where each transaction must be tracked by its posted date, ensuring accurate record-keeping and reporting across different ledger entries.
    """
    def __init__(self, ledger: Ledger, posting: Posting, balance: Quantity):
        self.ledger = ledger
        self.posting = posting
        self.balance = balance
        
    def date(self) -> datetime.date:
        """
        Date of the ledger entry.
        """
        return self.posting.date

# Test cases for LedgerEntry class
def test_ledger_entry_basic():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    posting_date = date.today()
    posting = Posting(date=posting_date)
    balance = Quantity()  # Assuming Quantity is defined elsewhere
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    
    assert entry.date() == posting_date

def test_ledger_entry_specific_date():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    specific_date = date(2023, 10, 15)
    posting = Posting(date=specific_date)
    balance = Quantity()  # Assuming Quantity is defined elsewhere
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    
    assert entry.date() == specific_date

def test_ledger_entry_with_specific_values():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    specific_date = date(2023, 10, 15)
    posting = Posting(date=specific_date)
    balance = Quantity()  # Assuming Quantity is defined elsewhere
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    
    assert entry.date() == specific_date

def test_ledger_entry_with_future_date():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    future_date = date(2100, 1, 1)  # A far-future date to ensure it's not the current date or a past date
    posting = Posting(date=future_date)
    balance = Quantity()  # Assuming Quantity is defined elsewhere
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    
    assert entry.date() == future_date

def test_ledger_entry_with_past_date():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    past_date = date(1900, 1, 1)  # A very old date to ensure it's not the current date or a future date
    posting = Posting(date=past_date)
    balance = Quantity()  # Assuming Quantity is defined elsewhere
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    
    assert entry.date() == past_date

def test_ledger_entry_no_posting():
    ledger = Ledger()  # Assuming Ledger is defined elsewhere
    with pytest.raises(AttributeError):  # Since posting should be available, this should raise an error
        entry = LedgerEntry(ledger=ledger, posting=None, balance=Quantity())
        entry.date()
