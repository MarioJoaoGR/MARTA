
import argparse
from environment import Environment
from exit_status import ExitStatus
import sys
import os
from typing import List, Union, Callable
from unittest.mock import patch

def raw_main(
    parser: argparse.ArgumentParser,
    main_program: Callable[[argparse.Namespace, Environment], ExitStatus],
    args: List[Union[str, bytes]] = sys.argv,
    env: Environment = Environment(),
    use_default_options: bool = True,
) -> ExitStatus:
    """
    Executes the main program logic based on command-line arguments and environment settings.
    
    This function processes command-line arguments, initializes the environment, loads installed plugins, parses arguments using a provided parser, handles errors gracefully, and executes the main program task if no daemon mode is enabled. It supports debug and traceback options for detailed error reporting during development.
    
    Parameters:
        parser (argparse.ArgumentParser): An argument parser object used to parse command-line arguments.
        main_program (Callable[[argparse.Namespace, Environment], ExitStatus]): A callable that takes parsed arguments and the environment as inputs and returns an exit status.
        args (List[Union[str, bytes]], optional): List of command-line arguments. Defaults to sys.argv if not provided.
        env (Environment, optional): An environment object representing the execution context, including standard streams and configuration settings. Defaults to a new Environment instance.
        use_default_options (bool, optional): A flag indicating whether to include default options in the argument list. Defaults to True.
    
    Returns:
        ExitStatus: The exit status of the program after executing the main task or handling errors. It can be SUCCESS, ERROR, ERROR_CTRL_C, ERROR_TIMEOUT, or ERROR_TOO_MANY_REDIRECTS depending on the outcome of the execution and error handling.
    
    Examples:
        To run the main function with a custom argument parser and program callable:
        
        ```python
        import argparse
        from environment import Environment
        from exit_status import ExitStatus
        
        # Define an argument parser
        parser = argparse.ArgumentParser()
        
        # Define a main program callable that takes parsed arguments and environment
        def main_program(args, env):
            # Example implementation of the main program logic
            print("Running main program with args:", args)
            return ExitStatus.SUCCESS
        
        # Call raw_main with the defined parser and main program callable
        result = raw_main(parser, main_program)
        ```
    
    Notes:
        - The function decodes command-line arguments if they are bytes objects using the specified encoding from the environment.
        - It checks for daemon mode and runs a daemon task if enabled; otherwise, it parses arguments, handles errors, and executes the main program logic.
        - Error handling includes generic error messages, detailed tracebacks, and specific status codes based on encountered exceptions.
    """
    program_name, *args = args
    env.program_name = os.path.basename(program_name)
    args = decode_raw_args(args, env.stdin_encoding)

    if is_daemon_mode(args):
        return run_daemon_task(env, args)

    plugin_manager.load_installed_plugins(env.config.plugins_dir)

    if use_default_options and env.config.default_options:
        args = env.config.default_options + args

    include_debug_info = '--debug' in args
    include_traceback = include_debug_info or '--traceback' in args

    def handle_generic_error(e, annotation=None):
        msg = str(e)
        if hasattr(e, 'request'):
            request = e.request
            if hasattr(request, 'url'):
                msg = (
                    f'{msg} while doing a {request.method}'
                    f' request to URL: {request.url}'
                )
        if annotation:
            msg += annotation
        env.log_error(f'{type(e).__name__}: {msg}')
        if include_traceback:
            raise

    if include_debug_info:
        print_debug_info(env)
        if args == ['--debug']:
            return ExitStatus.SUCCESS

    exit_status = ExitStatus.SUCCESS

    try:
        parsed_args = parser.parse_args(
            args=args,
            env=env,
        )
    except NestedJSONSyntaxError as exc:
        env.stderr.write(str(exc) + "\n")
        if include_traceback:
            raise
        exit_status = ExitStatus.ERROR
    except KeyboardInterrupt:
        env.stderr.write('\n')
        if include_traceback:
            raise
        exit_status = ExitStatus.ERROR_CTRL_C
    except SystemExit as e:
        if e.code != ExitStatus.SUCCESS:
            env.stderr.write('\n')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR
    else:
        check_updates(env)
        try:
            exit_status = main_program(
                args=parsed_args,
                env=env,
            )
        except KeyboardInterrupt:
            env.stderr.write('\n')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR_CTRL_C
        except SystemExit as e:
            if e.code != ExitStatus.SUCCESS:
                env.stderr.write('\n')
                if include_traceback:
                    raise
                exit_status = ExitStatus.ERROR
        except requests.Timeout:
            exit_status = ExitStatus.ERROR_TIMEOUT
            env.log_error(f'Request timed out ({parsed_args.timeout}s).')
        except requests.TooManyRedirects:
            exit_status = ExitStatus.ERROR_TOO_MANY_REDIRECTS
            env.log_error(
                f'Too many redirects'
                f' (--max-redirects={parsed_args.max_redirects}).'
            )
        except requests.exceptions.ConnectionError as exc:
            annotation = None
            original_exc = unwrap_context(exc)
            if isinstance(original_exc, socket.gaierror):
                if original_exc.errno == socket.EAI_AGAIN:
                    annotation = '\nCouldn’t connect to a DNS server. Please check your connection and try again.'
                elif original_exc.errno == socket.EAI_NONAME:
                    annotation = '\nCouldn’t resolve the given hostname. Please check the URL and try again.'
                propagated_exc = original_exc
            else:
                propagated_exc = exc

            handle_generic_error(propagated_exc, annotation=annotation)
            exit_status = ExitStatus.ERROR
        except Exception as e:
            # TODO: Further distinction between expected and unexpected errors.
            handle_generic_error(e)
            exit_status = ExitStatus.ERROR

    return exit_status

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_core_raw_main_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:3:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:4:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:60:11: E0602: Undefined variable 'decode_raw_args' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:62:7: E0602: Undefined variable 'is_daemon_mode' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:63:15: E0602: Undefined variable 'run_daemon_task' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:65:4: E0602: Undefined variable 'plugin_manager' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:86:12: E0704: The raise statement is not inside an except clause (misplaced-bare-raise)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:89:8: E0602: Undefined variable 'print_debug_info' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:100:11: E0602: Undefined variable 'NestedJSONSyntaxError' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:117:8: E0602: Undefined variable 'check_updates' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:134:15: E0602: Undefined variable 'requests' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:137:15: E0602: Undefined variable 'requests' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:143:15: E0602: Undefined variable 'requests' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:145:27: E0602: Undefined variable 'unwrap_context' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:146:40: E0602: Undefined variable 'socket' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:147:41: E0602: Undefined variable 'socket' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_core_raw_main_0_test_valid_inputs.py:149:43: E0602: Undefined variable 'socket' (undefined-variable)


"""