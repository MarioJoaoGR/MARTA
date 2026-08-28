
import pytest
from thonny.roughparse import RoughParser

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_find_good_parse_start_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        parser = RoughParser(indent_width=4, tabwidth=4)
>       parser.set_str('def example():\n\tprint("Hello, World!")')

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_find_good_parse_start_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.RoughParser object at 0x7f48977eba00>
s = 'def example():\n\tprint("Hello, World!")'

    def set_str(self, s):
>       assert len(s) == 0 or s[-1] == "\n"
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:168: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_find_good_parse_start_0.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""