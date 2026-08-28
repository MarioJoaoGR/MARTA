
import pytest
from flutils.txtutils import AnsiTextWrapper

def len_without_ansi(text):
    return len(strip_ansi(text))

def strip_ansi(text):
    if not text:
        return ""
    ansi_escape = re.compile(r'(?:\x1b\[[\d;]+[mGKH])')
    return ansi_escape.sub('', text)

@pytest.fixture
def setup_wrapper():
    wrapper = AnsiTextWrapper()
    yield wrapper



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_initial_indent_len_empty _________________________

setup_wrapper = <flutils.txtutils.AnsiTextWrapper object at 0x7f6b4ea484f0>

    def test_initial_indent_len_empty(setup_wrapper):
        wrapper = setup_wrapper
>       assert wrapper.initial_indent_len() == 0
E       TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py:21: TypeError
______________________ test_initial_indent_len_with_ansi _______________________

    def test_initial_indent_len_with_ansi():
        text = '\x1b[31mInitial Indent\x1b[0m'
        wrapper = AnsiTextWrapper(initial_indent=text)
>       assert wrapper.initial_indent_len() == len_without_ansi(text)
E       TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py:26: TypeError
__________________ test_initial_indent_len_no_initial_indent ___________________

    def test_initial_indent_len_no_initial_indent():
        wrapper = AnsiTextWrapper()
>       assert wrapper.initial_indent_len() == 0
E       TypeError: 'int' object is not callable

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py:30: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py::test_initial_indent_len_empty
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py::test_initial_indent_len_with_ansi
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_initial_indent_len_0.py::test_initial_indent_len_no_initial_indent
============================== 3 failed in 0.06s ===============================
"""