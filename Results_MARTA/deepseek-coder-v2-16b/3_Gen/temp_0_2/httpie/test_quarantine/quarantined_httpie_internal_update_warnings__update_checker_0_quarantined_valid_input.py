
from unittest.mock import patch, MagicMock
import httpie.internal.update_warnings

def _update_checker(func: Callable[[httpie.context.Environment], None]) -> Callable[[httpie.context.Environment], None]:
    """Control the execution of the update checker (suppress errors, trigger auto updates etc.)"""
    
    def wrapper(env: httpie.context.Environment) -> None:
        with patch.object(env, 'suppress_errors', return_value=None):
            func(env)
        
        with patch.object(env, 'suppress_errors', return_value=None):
            httpie.internal.update_warnings.maybe_fetch_updates(env)
    
    return wrapper

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_internal_update_warnings__update_checker_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__update_checker_0_test_valid_input.py:5:26: E0602: Undefined variable 'Callable' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__update_checker_0_test_valid_input.py:5:75: E0602: Undefined variable 'Callable' (undefined-variable)


"""