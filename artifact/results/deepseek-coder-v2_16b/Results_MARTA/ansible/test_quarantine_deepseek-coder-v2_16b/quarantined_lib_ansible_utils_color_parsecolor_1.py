
import pytest
from ansible.utils.color import parsecolor, C
import re



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_rgb246397 _____________________________

    def test_valid_rgb246397():
        color = 'rgb246397'
        expected_output = '38;5;190'
>       assert parsecolor(color) == expected_output

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = 'rgb246397'

    def parsecolor(color):
        """SGR parameter string for the specified color name."""
        matches = re.match(r"color(?P<color>[0-9]+)"
                           r"|(?P<rgb>rgb(?P<red>[0-5])(?P<green>[0-5])(?P<blue>[0-5]))"
                           r"|gray(?P<gray>[0-9]+)", color)
        if not matches:
>           return C.COLOR_CODES[color]
E           KeyError: 'rgb246397'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/color.py:62: KeyError
______________________________ test_valid_gray23 _______________________________

    def test_valid_gray23():
        color = 'gray23'
        expected_output = '38;5;23'
>       assert parsecolor(color) == expected_output
E       AssertionError: assert '38;5;255' == '38;5;23'
E         
E         - 38;5;23
E         ?       ^
E         + 38;5;255
E         ?       ^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py:14: AssertionError
______________________________ test_invalid_color ______________________________

    def test_invalid_color():
        color = 'unknown_color'
        with pytest.raises(ValueError):
>           parsecolor(color)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = 'unknown_color'

    def parsecolor(color):
        """SGR parameter string for the specified color name."""
        matches = re.match(r"color(?P<color>[0-9]+)"
                           r"|(?P<rgb>rgb(?P<red>[0-5])(?P<green>[0-5])(?P<blue>[0-5]))"
                           r"|gray(?P<gray>[0-9]+)", color)
        if not matches:
>           return C.COLOR_CODES[color]
E           KeyError: 'unknown_color'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/color.py:62: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py::test_valid_rgb246397
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py::test_valid_gray23
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_color_parsecolor_1.py::test_invalid_color
============================== 3 failed in 0.80s ===============================
"""