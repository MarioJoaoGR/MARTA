
import pytest
from tornado.util import re_unescape


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
>       assert re_unescape(r"\d+") == "\d+"

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tornado/tornado/util.py:230: in re_unescape
    return _re_unescape_pattern.sub(_re_unescape_replacement, s)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

match = <re.Match object; span=(0, 2), match='\\d'>

    def _re_unescape_replacement(match: Match[str]) -> str:
        group = match.group(1)
        if group[0] in _alphanum:
>           raise ValueError("cannot unescape '\\\\%s'" % group[0])
E           ValueError: cannot unescape '\\d'

/opt/marta/baselines/codamosa/replication/test-apps/tornado/tornado/util.py:214: ValueError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py:9: Failed
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py:6
  /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py:6: DeprecationWarning: invalid escape sequence '\d'
    assert re_unescape(r"\d+") == "\d+"

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_re_unescape_0.py::test_invalid_inputs
========================= 2 failed, 1 warning in 0.07s =========================
"""