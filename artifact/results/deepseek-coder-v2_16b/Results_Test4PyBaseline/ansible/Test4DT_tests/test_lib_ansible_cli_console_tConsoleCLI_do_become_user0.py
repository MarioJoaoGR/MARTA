
# Module: ansible.cli.console
# test_console_cli.py
from ansible.cli.console import ConsoleCLI
import pytest

@pytest.fixture(scope="module")
def console():
    return ConsoleCLI(['--inventory', 'path/to/inventory'])

def test_default_host_pattern(console):
    assert console.cwd == '*'

def test_change_host_pattern(console):
    console.do_cd('app*.dc*:!app01*')
    assert console.cwd == 'app*.dc*:!app01*'

def test_list_hosts(console):
    with pytest.raises(SystemExit):
        console.onecmd('list')
    # Assuming the list command would print hosts, we can check if the hosts are set correctly
    assert len(console.hosts) > 0

def test_become_user(console):
    console.do_become_user('root')
    assert console.become_user == 'root'
    # Assuming the prompt updates accordingly
    assert console.prompt == f"ansible ({console.cwd}) root> "

def test_help_command(console):
    with pytest.raises(SystemExit):
        console.onecmd('help cd')
    # Check if help output is as expected
    assert isinstance(console.stdout, str)  # Assuming stdout captures the help output
