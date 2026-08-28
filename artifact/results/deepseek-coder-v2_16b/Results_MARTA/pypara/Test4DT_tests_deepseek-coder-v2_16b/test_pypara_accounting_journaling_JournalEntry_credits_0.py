
import pytest
from datetime import date
from pypara.accounting.journaling import JournalEntry, Posting



def test_invalid_inputs():
    journal_entry = JournalEntry(date=date.today(), description='Invalid Entry', source='Source Unknown')
    with pytest.raises(AttributeError):
        journal_entry.postings = None