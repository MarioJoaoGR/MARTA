
import argparse
from httpie.sessions import Environment, ExitStatus
from unittest.mock import patch

def cli_upgrade_all_sessions(env: Environment, args: argparse.Namespace) -> ExitStatus:
    """
    Executes the 'upgrade-all' action for HTTP sessions across all hosts in the configuration directory.
    
    This function is designed to upgrade all HTTPie sessions stored in the configuration directory for each host. It iterates through each host's session files, identifies them as JSON files, and then attempts to upgrade each session using applicable fixers. The function accepts an environment configuration object (`env`) and command-line arguments (`args`), which are used for logging, output operations, and providing additional options or configurations to the fixers.
    
    Parameters:
        env (Environment): An environment configuration object that includes necessary settings and configurations for managing HTTP sessions.
        args (argparse.Namespace): Command-line arguments passed to the function, which are used to specify actions and provide additional options or configurations to the upgrade process.
    
    Returns:
        ExitStatus: The status of the operation after attempting to upgrade all sessions. It returns `ExitStatus.SUCCESS` if all sessions were successfully upgraded; otherwise, it returns `ExitStatus.ERROR`.
    
    Examples:
        To upgrade all sessions for all hosts in the configuration directory using an environment and arguments:
        ```python
        from httpie.sessions import Environment
        
        env = Environment()
        args = argparse.Namespace()  # Example arguments, replace with actual namespace if needed
        
        status = cli_upgrade_all_sessions(env, args)
        ```
    
    Notes:
        - The function operates by iterating through each host's session files in the configuration directory specified by `SESSIONS_DIR_NAME`.
        - For each session file found, it calls the `upgrade_session` function to upgrade the session.
        - If any session fails to upgrade, the overall status remains `ExitStatus.ERROR`; otherwise, it returns `ExitStatus.SUCCESS` after all sessions have been upgraded.
    """
    session_dir_path = env.config_dir / SESSIONS_DIR_NAME

    status = ExitStatus.SUCCESS
    for host_path in session_dir_path.iterdir():
        hostname = host_path.name
        for session_path in host_path.glob("*.json"):
            session_name = session_path.stem
            status |= upgrade_session(
                env,
                args=args,
                hostname=hostname,
                session_name=session_name
            )
    return status

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_sessions_cli_upgrade_all_sessions_1_test_invalid_inputs
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_sessions_cli_upgrade_all_sessions_1_test_invalid_inputs.py:3:0: E0611: No name 'ExitStatus' in module 'httpie.sessions' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_sessions_cli_upgrade_all_sessions_1_test_invalid_inputs.py:35:40: E0602: Undefined variable 'SESSIONS_DIR_NAME' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_sessions_cli_upgrade_all_sessions_1_test_invalid_inputs.py:42:22: E0602: Undefined variable 'upgrade_session' (undefined-variable)


"""