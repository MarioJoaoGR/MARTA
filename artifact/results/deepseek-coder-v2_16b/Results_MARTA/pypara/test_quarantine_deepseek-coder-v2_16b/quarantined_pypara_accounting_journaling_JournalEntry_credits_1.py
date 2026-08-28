
import pytest
from datetime import date
from pypara.accounting.journaling import JournalEntry, Posting



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_credits ______________________________

    def test_valid_credits():
        journal_entry = JournalEntry(date=date.today(), description='Sample Entry', source='Bank Statement')
>       journal_entry.postings = [Posting(-100, 'DEC'), Posting(50, 'INC')]
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py:8: TypeError
______________________________ test_empty_credits ______________________________

    def test_empty_credits():
        journal_entry = JournalEntry(date=date.today(), description='Empty Entry', source='Personal Account')
>       journal_entry.postings = [Posting(-100, 'DEC')]
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py:15: TypeError
_____________________________ test_invalid_credits _____________________________

    def test_invalid_credits():
        journal_entry = JournalEntry(date=date.today(), description='Invalid Entry', source='Credit Card Statement')
        with pytest.raises(AttributeError):
>           credits = list(journal_entry.credits())
E           TypeError: 'generator' object is not callable

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py::test_valid_credits
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py::test_empty_credits
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_credits_1.py::test_invalid_credits
============================== 3 failed in 0.07s ===============================
"""