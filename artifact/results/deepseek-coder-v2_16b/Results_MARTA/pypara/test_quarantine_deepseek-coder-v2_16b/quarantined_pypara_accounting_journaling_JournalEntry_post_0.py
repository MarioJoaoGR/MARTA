
import pytest
from datetime import date
from pypara.accounting import Account, Quantity, JournalEntry

# Test scenario 1: Posting a positive quantity to an account
def test_post_positive_quantity():
    journal_entry = JournalEntry()
    account = Account()
    quantity = Quantity(100)
    
    result = journal_entry.post(date=date.today(), account=account, quantity=quantity)
    
    assert len(journal_entry.postings) == 1
    assert journal_entry.postings[0].amount == 100
    assert journal_entry.postings[0].direction == 'credit'
    assert result == journal_entry

# Test scenario 2: Posting a negative quantity to an account
def test_post_negative_quantity():
    journal_entry = JournalEntry()
    account = Account()
    quantity = Quantity(-50)
    
    result = journal_entry.post(date=date.today(), account=account, quantity=quantity)
    
    assert len(journal_entry.postings) == 1
    assert journal_entry.postings[0].amount == 50
    assert journal_entry.postings[0].direction == 'debit'
    assert result == journal_entry

# Test scenario 3: Posting a zero quantity does not change the journal entry
def test_post_zero_quantity():
    journal_entry = JournalEntry()
    account = Account()
    quantity = Quantity(0)
    
    initial_postings_count = len(journal_entry.postings)
    result = journal_entry.post(date=date.today(), account=account, quantity=quantity)
    
    assert len(journal_entry.postings) == initial_postings_count
    assert result == journal_entry

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
__ ERROR collecting test_pypara_accounting_journaling_JournalEntry_post_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_post_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_post_0.py:4: in <module>
    from pypara.accounting import Account, Quantity, JournalEntry
E   ImportError: cannot import name 'Account' from 'pypara.accounting' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/accounting/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_post_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""