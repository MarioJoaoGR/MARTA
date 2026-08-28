
import pytest
from datetime import date
from pypara.accounting.journaling import JournalEntry, Posting

class TestJournalEntryIncrements:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
        self.posting1 = Posting(-100, 'DEC')
        self.posting2 = Posting(50, 'INC')
        self.journal_entry.postings = [self.posting1, self.posting2]
    
    def test_increments_returns_only_increment_postings(self):
        increment_postings = list(self.journal_entry.increments())
        assert len(increment_postings) == 1
        assert increment_postings[0].amount == 50
        assert increment_postings[0].direction == 'INC'
    
    def test_increments_returns_correct_increment_amounts(self):
        increment_postings = list(self.journal_entry.increments())
        assert len(increment_postings) == 1
        assert increment_postings[0].amount == 50
        assert increment_postings[0].direction == 'INC'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_increments_0.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_ ERROR at setup of TestJournalEntryIncrements.test_increments_returns_only_increment_postings _

self = <test_pypara_accounting_journaling_JournalEntry_increments_0.TestJournalEntryIncrements object at 0x7f270a480340>

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
>       self.posting1 = Posting(-100, 'DEC')
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_increments_0.py:11: TypeError
_ ERROR at setup of TestJournalEntryIncrements.test_increments_returns_correct_increment_amounts _

self = <test_pypara_accounting_journaling_JournalEntry_increments_0.TestJournalEntryIncrements object at 0x7f270a480850>

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.journal_entry = JournalEntry(date=date.today(), description="Sample Entry", source="Bank Statement")
>       self.posting1 = Posting(-100, 'DEC')
E       TypeError: Posting.__init__() missing 3 required positional arguments: 'account', 'direction', and 'amount'

/opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_increments_0.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_increments_0.py::TestJournalEntryIncrements::test_increments_returns_only_increment_postings
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pypara/Test4DT_tests_deepseek-coder-v2_16b/test_pypara_accounting_journaling_JournalEntry_increments_0.py::TestJournalEntryIncrements::test_increments_returns_correct_increment_amounts
============================== 2 errors in 0.08s ===============================
"""