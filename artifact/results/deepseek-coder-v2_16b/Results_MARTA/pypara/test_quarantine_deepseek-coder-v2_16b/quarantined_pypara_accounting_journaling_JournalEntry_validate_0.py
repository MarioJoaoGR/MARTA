
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

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        journal_entry = JournalEntry(date=date.today(), description='Sample Entry', source='Bank Statement')
>       journal_entry.postings = [Posting(-100, 'DEC'), Posting(100, 'INC')]
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py:8: TypeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        journal_entry = JournalEntry(date=date.today(), description='Sample Entry', source='Bank Statement')
>       journal_entry.postings = [None, Posting(0, 'INC')]
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py:13: TypeError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        journal_entry = JournalEntry(date=date.today(), description='Sample Entry', source='Bank Statement')
>       journal_entry.postings = [Posting(-50, 'DEC'), Posting(30, 'INC')]
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py:19: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_validate_0.py::test_invalid_inputs
============================== 3 failed in 0.06s ===============================
"""