
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import print_debug_info
import sys
import platform

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.core.Environment') as MockEnvironment:
        env = MockEnvironment.return_value
        env.stderr = MagicMock()
        yield env

def test_valid_input(mock_environment):
    print_debug_info(mock_environment)
    
    # Assertions to verify the mock environment's stderr output
    expected_output = [
        f'HTTPie {httpie_version}\n',
        f'Requests {requests_version}\n',
        f'Pygments {pygments_version}\n',
        f'Python {sys.version}\n{sys.executable}\n',
        f'{platform.system()} {platform.release()}',
    ]
    
    for expected in expected_output:
        mock_environment.stderr.writelines.assert_any_call(expected)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_core_print_debug_info_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_core_print_debug_info_0_test_valid_input.py:20:18: E0602: Undefined variable 'httpie_version' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_print_debug_info_0_test_valid_input.py:21:20: E0602: Undefined variable 'requests_version' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_print_debug_info_0_test_valid_input.py:22:20: E0602: Undefined variable 'pygments_version' (undefined-variable)


"""