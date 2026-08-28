
import argparse
from ansible.cli.arguments.option_helpers import add_connect_options
import pytest

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_connect_options_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_add_connect_options ___________________________

    def test_add_connect_options():
        parser = argparse.ArgumentParser()
        add_connect_options(parser)
>       args = parser.parse_args(['--help'])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_connect_options_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1833: in parse_args
    args, argv = self.parse_known_args(args, namespace)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1866: in parse_known_args
    namespace, args = self._parse_known_args(args, namespace)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2079: in _parse_known_args
    start_index = consume_optional(start_index)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2019: in consume_optional
    take_action(action, args, option_string)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1943: in take_action
    action(self, namespace, argument_values, option_string)
/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:1107: in __call__
    parser.exit()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = ArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
status = 0, message = None

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
>       _sys.exit(status)
E       SystemExit: 0

/opt/conda/envs/test4py_env/lib/python3.10/argparse.py:2581: SystemExit
----------------------------- Captured stdout call -----------------------------
usage: __main__.py [-h] [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER]
                   [-c CONNECTION] [-T TIMEOUT]
                   [--ssh-common-args SSH_COMMON_ARGS]
                   [--sftp-extra-args SFTP_EXTRA_ARGS]
                   [--scp-extra-args SCP_EXTRA_ARGS]
                   [--ssh-extra-args SSH_EXTRA_ARGS]
                   [-k | --connection-password-file CONNECTION_PASSWORD_FILE]

options:
  -h, --help            show this help message and exit
  -k, --ask-pass        ask for connection password
  --connection-password-file CONNECTION_PASSWORD_FILE, --conn-pass-file CONNECTION_PASSWORD_FILE
                        Connection password file

Connection Options:
  control as whom and how to connect to hosts

  --private-key PRIVATE_KEY_FILE, --key-file PRIVATE_KEY_FILE
                        use this file to authenticate the connection
  -u REMOTE_USER, --user REMOTE_USER
                        connect as this user (default=None)
  -c CONNECTION, --connection CONNECTION
                        connection type to use (default=smart)
  -T TIMEOUT, --timeout TIMEOUT
                        override the connection timeout in seconds
                        (default=10)
  --ssh-common-args SSH_COMMON_ARGS
                        specify common arguments to pass to sftp/scp/ssh (e.g.
                        ProxyCommand)
  --sftp-extra-args SFTP_EXTRA_ARGS
                        specify extra arguments to pass to sftp only (e.g. -f,
                        -l)
  --scp-extra-args SCP_EXTRA_ARGS
                        specify extra arguments to pass to scp only (e.g. -l)
  --ssh-extra-args SSH_EXTRA_ARGS
                        specify extra arguments to pass to ssh only (e.g. -R)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_connect_options_0.py::test_add_connect_options
============================== 1 failed in 0.70s ===============================
"""