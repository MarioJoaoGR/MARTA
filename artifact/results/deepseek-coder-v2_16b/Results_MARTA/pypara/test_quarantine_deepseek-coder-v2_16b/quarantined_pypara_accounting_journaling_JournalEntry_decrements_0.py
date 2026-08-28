
import pytest
from datetime import date
from typing import List, Iterable
import uuid

# Assuming these classes and methods are defined in a module named 'pypara.accounting.journaling'
class Posting:
    def __init__(self, amount: float, direction: str):
        self.amount = amount
        self.direction = direction
    
    def __repr__(self):
        return f"Posting(amount={self.amount}, direction={self.direction})"

class JournalEntry:
    def __init__(self, date: datetime.date, description: str, source: _T, postings: List[Posting] = None, guid: uuid.UUID = None):
        self.date = date
        self.description = description
        self.source = source
        if postings is None:
            postings = []
        self.postings = postings
        if guid is None:
            guid = uuid.uuid4()
        self.guid = guid
    
    def increments(self) -> Iterable[Posting]:
        return (p for p in self.postings if p.direction == 'INC')
    
    def decrements(self) -> Iterable[Posting]:
        return (p for p in self.postings if p.direction == 'DEC')
    
    def debits(self) -> Iterable[Posting]:
        return (p for p in self.postings if p.amount < 0)
    
    def credits(self) -> Iterable[Posting]:
        return (p for p in self.postings if p.amount > 0)

# Test cases for JournalEntry class
def test_journal_entry_initialization():
    journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
    assert journal_entry.description == "Sample Entry"
    assert journal_entry.source == "Bank Statement"
    assert len(journal_entry.postings) == 0
    assert isinstance(journal_entry.guid, uuid.UUID)

def test_increment_events():
    journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
    journal_entry.postings = [Posting(-100, 'DEC'), Posting(50, 'INC')]
    
    increments = list(journal_entry.increments())
    assert len(increments) == 1
    assert increments[0].amount == 50
    assert increments[0].direction == 'INC'

def test_decrement_events():
    journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
    journal_entry.postings = [Posting(-100, 'DEC'), Posting(50, 'INC')]
    
    decrements = list(journal_entry.decrements())
    assert len(decrements) == 1
    assert decrements[0].amount == -100
    assert decrements[0].direction == 'DEC'

def test_debit_events():
    journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
    journal_entry.postings = [Posting(-100, 'DEC'), Posting(50, 'INC')]
    
    debits = list(journal_entry.debits())
    assert len(debits) == 1
    assert debits[0].amount == -100
    assert debits[0].direction == 'DEC'

def test_credit_events():
    journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
    journal_entry.postings = [Posting(-100, 'DEC'), Posting(50, 'INC')]
    
    credits = list(journal_entry.credits())
    assert len(credits) == 1
    assert credits[0].amount == 50
    assert credits[0].direction == 'INC'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_pypara_accounting_journaling_JournalEntry_decrements_0.py _
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_decrements_0.py:16: in <module>
    class JournalEntry:
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_decrements_0.py:17: in JournalEntry
    def __init__(self, date: datetime.date, description: str, source: _T, postings: List[Posting] = None, guid: uuid.UUID = None):
E   NameError: name 'datetime' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_decrements_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""