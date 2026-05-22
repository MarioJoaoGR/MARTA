
import pytest
from unittest.mock import patch
from httpie.manager.cli import COMMANDS, missing_subcommand

@pytest.mark.parametrize("args, expected_message", [
    (['git'], "Please specify one of these: 'status', 'clone'..."),
    (['git', 'status'], "Please specify one of these: 'add', 'commit'...")
])
def test_error_input(args, expected_message):
    with patch('httpie.manager.cli.COMMANDS', {
        'git': {
            'status': {'add': {}, 'commit': {}},
            'clone': {}
        }
    }):
        assert missing_subcommand(*args) == expected_message

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

httpie/Test4DT_tests_codestral/test_httpie_manager_cli_missing_subcommand_0_test_error_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__ test_error_input[args0-Please specify one of these: 'status', 'clone'...] ___

args = ['git']
expected_message = "Please specify one of these: 'status', 'clone'..."

    @pytest.mark.parametrize("args, expected_message", [
        (['git'], "Please specify one of these: 'status', 'clone'..."),
        (['git', 'status'], "Please specify one of these: 'add', 'commit'...")
    ])
    def test_error_input(args, expected_message):
        with patch('httpie.manager.cli.COMMANDS', {
            'git': {
                'status': {'add': {}, 'commit': {}},
                'clone': {}
            }
        }):
>           assert missing_subcommand(*args) == expected_message
E           assert "Please speci...tus', 'clone'" == "Please speci...', 'clone'..."
E             
E             Skipping 35 identical leading characters in diff, use -v to show
E             - s', 'clone'...
E             ?            ---
E             + s', 'clone'

httpie/Test4DT_tests_codestral/test_httpie_manager_cli_missing_subcommand_0_test_error_input.py:17: AssertionError
___ test_error_input[args1-Please specify one of these: 'add', 'commit'...] ____

args = ['git', 'status']
expected_message = "Please specify one of these: 'add', 'commit'..."

    @pytest.mark.parametrize("args, expected_message", [
        (['git'], "Please specify one of these: 'status', 'clone'..."),
        (['git', 'status'], "Please specify one of these: 'add', 'commit'...")
    ])
    def test_error_input(args, expected_message):
        with patch('httpie.manager.cli.COMMANDS', {
            'git': {
                'status': {'add': {}, 'commit': {}},
                'clone': {}
            }
        }):
>           assert missing_subcommand(*args) == expected_message
E           assert "Please speci...dd', 'commit'" == "Please speci..., 'commit'..."
E             
E             Skipping 33 identical leading characters in diff, use -v to show
E             - ', 'commit'...
E             ?            ---
E             + ', 'commit'

httpie/Test4DT_tests_codestral/test_httpie_manager_cli_missing_subcommand_0_test_error_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_cli_missing_subcommand_0_test_error_input.py::test_error_input[args0-Please specify one of these: 'status', 'clone'...]
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_cli_missing_subcommand_0_test_error_input.py::test_error_input[args1-Please specify one of these: 'add', 'commit'...]
============================== 2 failed in 0.20s ===============================
"""