
import pytest
from unittest.mock import patch
from io import StringIO  # Corrected import for StringIO
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console():
    return ConsoleCLI({})

@pytest.mark.parametrize("args, expected", [
    ({'host-pattern': 'app*.dc*:!app01*'}, "Starting with host pattern: app*.dc*:!app01*"),
    ({'verbosity': 3}, "Setting verbosity level to 3")
])
def test_custom_configuration(console, args, expected):
    with patch('sys.stdout', new=StringIO()) as fake_output:  # Corrected usage of StringIO
        console = ConsoleCLI(args)
        console.cmdloop()
        assert expected in fake_output.getvalue()

@pytest.mark.parametrize("command", [
    "cd app*.dc*",
    "list",
    "list groups",
    "become",
    "! yum update -y",
    "verbosity 3",
    "forks 5",
    "become_user root",
    "remote_user ansible",
    "become_method sudo",
    "check True",
    "diff False",
    "timeout 60",
    "help cd",
    "exit"
])
def test_commands(console, command):
    with patch('sys.stdout', new=StringIO()) as fake_output:  # Corrected usage of StringIO
        console = ConsoleCLI({})
        console.onecmd(command)
        assert "Command not recognized" not in fake_output.getvalue()

if __name__ == "__main__":
    pytest.main()
