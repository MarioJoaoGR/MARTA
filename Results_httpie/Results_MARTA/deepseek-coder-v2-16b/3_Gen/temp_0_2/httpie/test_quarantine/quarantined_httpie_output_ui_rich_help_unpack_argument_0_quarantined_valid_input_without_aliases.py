
import pytest
from httpie.output.ui.rich_help import unpack_argument, Argument, Text

@pytest.fixture
def argument():
    return Argument(aliases=['-f', '--file'], metavar='FILE')

def test_unpack_argument_with_aliases(argument):
    opt1, opt2 = unpack_argument(argument)
    assert str(opt1) == '-f'
    assert str(opt2) == '-f'

def test_unpack_argument_without_aliases():
    argument = Argument(metavar='FILE')
    opt1, opt2 = unpack_argument(argument)
    assert str(opt1) == 'FILE'
    assert str(opt2) == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_unpack_argument_0_test_valid_input_without_aliases.py E [ 50%]
F                                                                        [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_unpack_argument_with_aliases ______________

    @pytest.fixture
    def argument():
>       return Argument(aliases=['-f', '--file'], metavar='FILE')
E       TypeError: Argument.__new__() got an unexpected keyword argument 'metavar'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_unpack_argument_0_test_valid_input_without_aliases.py:7: TypeError
=================================== FAILURES ===================================
_____________________ test_unpack_argument_without_aliases _____________________

    def test_unpack_argument_without_aliases():
>       argument = Argument(metavar='FILE')
E       TypeError: Argument.__new__() got an unexpected keyword argument 'metavar'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_unpack_argument_0_test_valid_input_without_aliases.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_unpack_argument_0_test_valid_input_without_aliases.py::test_unpack_argument_without_aliases
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_unpack_argument_0_test_valid_input_without_aliases.py::test_unpack_argument_with_aliases
========================== 1 failed, 1 error in 0.35s ==========================
"""