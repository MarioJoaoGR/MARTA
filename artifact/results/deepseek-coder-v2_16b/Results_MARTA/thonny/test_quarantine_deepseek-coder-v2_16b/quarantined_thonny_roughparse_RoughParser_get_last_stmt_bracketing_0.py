
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.set_str("def example():\n\tprint('Hello, World!')\n")
    
        assert parser._tran1 == {
            ord('('): ord('('), ord('{'): ord('('), ord('['): ord('('),
            ord(')'): ord(')'), ord('}'): ord(')'), ord(']'): ord(')'),
            ord('"'): ord('"'), ord("'"): ord("'"), ord('\\'): ord('\\'), ord('\n'): ord('\n'), ord('#'): ord('#')
        }
    
>       assert parser.get_continuation_type() == 'newline'
E       AssertionError: assert 0 == 'newline'
E        +  where 0 = get_continuation_type()
E        +    where get_continuation_type = <thonny.roughparse.RoughParser object at 0x7fa43213e920>.get_continuation_type

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py:15: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.set_str("")
    
        assert parser._tran1 == {
            ord('('): ord('('), ord('{'): ord('('), ord('['): ord('('),
            ord(')'): ord(')'), ord('}'): ord(')'), ord(']'): ord(')'),
            ord('"'): ord('"'), ord("'"): ord("'"), ord('\\'): ord('\\'), ord('\n'): ord('\n'), ord('#'): ord('#')
        }
    
>       assert parser.get_continuation_type() == 'none'
E       AssertionError: assert 0 == 'none'
E        +  where 0 = get_continuation_type()
E        +    where get_continuation_type = <thonny.roughparse.RoughParser object at 0x7fa43213fe50>.get_continuation_type

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py:27: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        with pytest.raises(ValueError):
            parser = RoughParser(indent_width=4, tabwidth=4)
>           parser.set_str("invalid code")

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <thonny.roughparse.RoughParser object at 0x7fa43213f700>
s = 'invalid code'

    def set_str(self, s):
>       assert len(s) == 0 or s[-1] == "\n"
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:168: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse_RoughParser_get_last_stmt_bracketing_0.py::test_error_case
============================== 3 failed in 0.06s ===============================
"""