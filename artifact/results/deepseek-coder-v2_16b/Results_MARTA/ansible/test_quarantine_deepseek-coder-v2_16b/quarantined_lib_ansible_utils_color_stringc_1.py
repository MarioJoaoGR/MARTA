
import pytest
from ansible.utils.color import stringc




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________________ test_stringc_basic ______________________________

    def test_stringc_basic():
        result = stringc("Hello, World!", "color256")
>       assert "\033[38;5;256mHello, World!\033[0m" == result
E       AssertionError: assert '\x1b[38;5;25...World!\x1b[0m' == 'Hello, World!'
E         
E         - Hello, World!
E         + [38;5;256mHello, World![0m

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py:7: AssertionError
____________________________ test_stringc_multiline ____________________________

    def test_stringc_multiline():
        multi_line_text = "Multi-line\ntext"
        result = stringc(multi_line_text, "rgb246397", wrap_nonvisible_chars=True)
>       assert "\001\033[38;5;190m\002Multi-line\n\001\033[38;5;190m\002text\033[0m" == result
E       AssertionError: assert '\x01\x1b[38;...02text\x1b[0m' == 'Multi-line\ntext'
E         
E         - Multi-line
E         - text
E         + [38;5;190mMulti-line
E         + [38;5;190mtext[0m

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py:12: AssertionError
______________________________ test_stringc_plain ______________________________

    def test_stringc_plain():
        plain_text = "Plain text"
        result = stringc(plain_text, "gray23")
>       assert "\033[38;5;23mPlain text\033[0m" == result
E       AssertionError: assert '\x1b[38;5;23...n text\x1b[0m' == 'Plain text'
E         
E         - Plain text
E         + [38;5;23mPlain text[0m

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py:17: AssertionError
_____________________________ test_stringc_nowrap ______________________________

    def test_stringc_nowrap():
        result = stringc("Hello, World!", "color256", wrap_nonvisible_chars=False)
>       assert "\033[38;5;256mHello, World!\033[0m" == result
E       AssertionError: assert '\x1b[38;5;25...World!\x1b[0m' == 'Hello, World!'
E         
E         - Hello, World!
E         + [38;5;256mHello, World![0m

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py::test_stringc_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py::test_stringc_multiline
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py::test_stringc_plain
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_stringc_1.py::test_stringc_nowrap
============================== 4 failed in 0.78s ===============================
"""