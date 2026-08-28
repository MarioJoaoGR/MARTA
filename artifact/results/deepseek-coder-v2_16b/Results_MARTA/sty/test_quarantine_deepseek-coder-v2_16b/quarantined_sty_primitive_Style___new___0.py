
import pytest
from sty import Style, RgbFg, Sgr


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Style___new___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        style = Style(RgbFg(1, 5, 10), Sgr(1))
        assert isinstance(style, Style)
>       assert str(style) == '\x1b[38;2;1;5;10m\x1b[1m'
E       AssertionError: assert '' == '\x1b[38;2;1;5;10m\x1b[1m'
E         
E         - [38;2;1;5;10m[1m

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Style___new___0.py:8: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Style___new___0.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Style___new___0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Style___new___0.py::test_invalid_input
============================== 2 failed in 0.04s ===============================
"""