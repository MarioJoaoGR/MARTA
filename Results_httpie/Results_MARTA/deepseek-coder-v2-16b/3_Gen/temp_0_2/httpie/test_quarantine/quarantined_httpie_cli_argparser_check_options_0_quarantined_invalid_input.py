
import pytest
from httpie.cli.argparser import OUTPUT_OPTIONS

@pytest.mark.parametrize("value, option, expected_error", [
    (set(), 'output', "Unknown output options: output="),
    (set(['a']), 'output', "Unknown output options: output=a"),
    (set(['b']), 'output', "Unknown output options: output=b"),
    (set(['c']), 'output', "Unknown output options: output=c")
])
def test_invalid_input(value, option, expected_error):
    with pytest.raises(ValueError) as excinfo:
        check_options(value, option)
    assert str(excinfo.value) == expected_error

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_argparser_check_options_0_test_invalid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_check_options_0_test_invalid_input.py:13:8: E0602: Undefined variable 'check_options' (undefined-variable)


"""