
import pytest
from pypara.accounting.ledger import Ledger, Account, Balance, Posting, Transaction, LedgerEntry, Quantity

# Test adding a new ledger entry with initial balance and posting
def test_add_new_entry():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    posting = Posting(Transaction(50, 'credit'), Transaction('credit', 50))
    new_entry = ledger.add(posting)
    
    assert isinstance(new_entry, LedgerEntry)
    assert new_entry.balance == Quantity(150)
    assert len(ledger.entries) == 1

# Test adding a new ledger entry with existing entries and balance calculation
def test_add_with_existing_entries():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    entry1 = LedgerEntry(ledger, Posting(Transaction(50, 'credit'), Transaction('credit', 50)), Balance(150))
    entry2 = LedgerEntry(ledger, Posting(Transaction(-30, 'debit'), Transaction('debit', -30)), Balance(120))
    ledger.entries = [entry1, entry2]
    
    posting = Posting(Transaction(20, 'credit'), Transaction('credit', 20))
    new_entry = ledger.add(posting)
    
    assert isinstance(new_entry, LedgerEntry)
    assert new_entry.balance == Quantity(140)
    assert len(ledger.entries) == 3

# Test adding a new ledger entry with no existing entries (initial balance only)
def test_add_with_no_existing_entries():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    
    posting = Posting(Transaction(50, 'credit'), Transaction('credit', 50))
    new_entry = ledger.add(posting)
    
    assert isinstance(new_entry, LedgerEntry)
    assert new_entry.balance == Quantity(150)
    assert len(ledger.entries) == 1

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
________ ERROR collecting test_pypara_accounting_ledger_Ledger_add_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger_add_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger_add_0.py:3: in <module>
    from pypara.accounting.ledger import Ledger, Account, Balance, Posting, Transaction, LedgerEntry, Quantity
E   ImportError: cannot import name 'Transaction' from 'pypara.accounting.ledger' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/accounting/ledger.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger_add_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""