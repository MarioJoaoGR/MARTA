
import pytest
from datetime import date
from pypara.accounting import Ledger, Posting, Quantity, Amount, Account

# Test initialization of LedgerEntry
def test_ledger_entry_initialization():
    ledger_instance = Ledger()
    posting_instance = Posting(date=date.today(), amount=Amount(100), account=Account("Assets"))
    balance_instance = Quantity(value=100)
    
    ledger_entry_instance = LedgerEntry(ledger=ledger_instance, posting=posting_instance, balance=balance_instance)
    
    assert isinstance(ledger_entry_instance.ledger, Ledger)
    assert isinstance(ledger_entry_instance.posting, Posting)
    assert isinstance(ledger_entry_instance.balance, Quantity)

# Test the date method of LedgerEntry
def test_ledger_entry_date():
    ledger_instance = Ledger()
    posting_date = date.today()
    posting_instance = Posting(date=posting_date, amount=Amount(100), account=Account("Assets"))
    balance_instance = Quantity(value=100)
    
    ledger_entry_instance = LedgerEntry(ledger=ledger_instance, posting=posting_instance, balance=balance_instance)
    
    assert ledger_entry_instance.date() == posting_date

# Test the date method of LedgerEntry with a specific date
def test_ledger_entry_specific_date():
    specific_date = date(2023, 10, 1)
    ledger_instance = Ledger()
    posting_instance = Posting(date=specific_date, amount=Amount(100), account=Account("Assets"))
    balance_instance = Quantity(value=100)
    
    ledger_entry_instance = LedgerEntry(ledger=ledger_instance, posting=posting_instance, balance=balance_instance)
    
    assert ledger_entry_instance.date() == specific_date

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
_____ ERROR collecting test_pypara_accounting_ledger_LedgerEntry_date_0.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_date_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_date_0.py:4: in <module>
    from pypara.accounting import Ledger, Posting, Quantity, Amount, Account
E   ImportError: cannot import name 'Ledger' from 'pypara.accounting' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/accounting/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_date_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""