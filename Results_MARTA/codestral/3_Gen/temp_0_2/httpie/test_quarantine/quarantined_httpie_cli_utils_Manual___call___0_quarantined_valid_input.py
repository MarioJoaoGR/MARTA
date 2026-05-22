
import argparse
from httpie.cli.utils import Manual

def test_valid_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', action=Manual, help='Prints the manual page.')
    
    # Test with valid input
    args = ['--manual']
    with pytest.raises(SystemExit):
        parser.parse_args(args)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_utils_Manual___call___0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_utils_Manual___call___0_test_valid_input.py:11:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""