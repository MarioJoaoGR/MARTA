
import sys
from typing import List, Union
from environment import Environment
from exit_status import ExitStatus
from httpie.core import main as raw_main
from .cli.definition import parser

def main(
    args: List[Union[str, bytes]] = sys.argv,
    env: Environment = Environment()
) -> ExitStatus:
    """
    The main function.

    Pre-process args, handle some special types of invocations,
    and run the main program with error handling.

    Return exit status code.

    """
    return raw_main(
        parser=parser,
        main_program=sys.modules['httpie.core'].__dict__['main'],
        args=args,
        env=env
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_core_main_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_main_0_test_valid_inputs.py:4:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_main_0_test_valid_inputs.py:5:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_main_0_test_valid_inputs.py:7:0: E0401: Unable to import 'Test4DT_tests_deepseek-coder-v2_16b.cli.definition' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_main_0_test_valid_inputs.py:22:11: E1123: Unexpected keyword argument 'parser' in function call (unexpected-keyword-arg)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_main_0_test_valid_inputs.py:22:11: E1123: Unexpected keyword argument 'main_program' in function call (unexpected-keyword-arg)


"""