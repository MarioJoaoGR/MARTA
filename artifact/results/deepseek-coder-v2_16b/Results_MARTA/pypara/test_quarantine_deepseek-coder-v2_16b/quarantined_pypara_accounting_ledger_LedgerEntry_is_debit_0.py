
import pytest
from pypara.accounting import Ledger, Posting, Quantity

# Test for LedgerEntry is_debit method when posting is a debit
def test_ledger_entry_is_debit_true():
    ledger = Ledger()
    posting = Posting(date=None, amount=Quantity(100), account="Assets")
    balance = Quantity(value=100)
    ledger_entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    assert ledger_entry.is_debit() is True

# Test for LedgerEntry is_debit method when posting is a credit
def test_ledger_entry_is_debit_false():
    ledger = Ledger()
    posting = Posting(date=None, amount=Quantity(-100), account="Liabilities")
    balance = Quantity(value=-100)
    ledger_entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    assert ledger_entry.is_debit() is False

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
___ ERROR collecting test_pypara_accounting_ledger_LedgerEntry_is_debit_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_is_debit_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_is_debit_0.py:3: in <module>
    from pypara.accounting import Ledger, Posting, Quantity
E   ImportError: cannot import name 'Ledger' from 'pypara.accounting' (/opt/marta/baselines/codamosa/replication/test-apps/pypara/pypara/accounting/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_ledger_LedgerEntry_is_debit_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""