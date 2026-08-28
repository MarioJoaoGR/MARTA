
import pytest
from unittest.mock import patch
from pypara.accounting.ledger import Ledger, Account, Balance, LedgerEntry, Transaction, Posting

# Test case for _last_balance method when there are no entries in the ledger
def test_last_balance_no_entries():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    assert ledger._last_balance() == Balance(100)

# Test case for _last_balance method when there are entries in the ledger
def test_last_balance_with_entries():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    entry1 = LedgerEntry(amount=Transaction(50, "credit"), balance=Balance(150))
    entry2 = LedgerEntry(amount=Transaction(-30, "debit"), balance=Balance(120))
    ledger.entries = [entry1, entry2]
    assert ledger._last_balance() == Balance(120)

# Test case for _last_balance method when there are no entries and initial balance is expected
def test_last_balance_no_entries_initial_balance():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    assert ledger._last_balance() == Balance(100)

# Test case for _last_balance method when there are entries and the last balance is expected
def test_last_balance_with_entries_expected_balance():
    ledger = Ledger(initial=Balance(100), account=Account("Main"))
    entry1 = LedgerEntry(amount=Transaction(50, "credit"), balance=Balance(150))
    entry2 = LedgerEntry(amount=Transaction(-30, "debit"), balance=Balance(120))
    ledger.entries = [entry1, entry2]
    assert ledger._last_balance() == Balance(120)

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
___ ERROR collecting test_pypara_accounting_ledger_Ledger__last_balance_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger__last_balance_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger__last_balance_0.py:4: in <module>
    from pypara.accounting.ledger import Ledger, Account, Balance, LedgerEntry, Transaction, Posting
E   ImportError: cannot import name 'Transaction' from 'pypara.accounting.ledger' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/accounting/ledger.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_Ledger__last_balance_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""