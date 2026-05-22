
import argparse
from environment import Environment
from exit_status import ExitStatus
from httpie.manager.core import dispatch_cli_task

def program(args: argparse.Namespace, env: Environment) -> ExitStatus:
    if args.action is None:
        parser.error("Error: a subcommand is missing")

    if args.action == 'plugins':
        return dispatch_cli_task(env, args.action, args)
    elif args.action == 'cli':
        return dispatch_cli_task(env, args.cli_action, args)

    return ExitStatus.SUCCESS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_core_program_0_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_manager_core_program_0_test_invalid_inputs.py:3:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_core_program_0_test_invalid_inputs.py:4:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_core_program_0_test_invalid_inputs.py:9:8: E0602: Undefined variable 'parser' (undefined-variable)


"""