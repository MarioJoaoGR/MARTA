
# Module: ansible.cli.console
# test_consolecli.py
from ansible.cli.console import ConsoleCLI
import pytest

@pytest.fixture(scope="module")
def console():
    return ConsoleCLI({'host-pattern': 'app*.dc*:!app01*'})

def test_cd_command(console):
    # Test changing to a valid host pattern
    with pytest.raises(SystemExit) as e:
        console.onecmd('cd app*.dc*')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_list_command(console):
    # Test listing hosts in the current path
    with pytest.raises(SystemExit) as e:
        console.onecmd('list')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_list_groups_command(console):
    # Test listing groups in the current path
    with pytest.raises(SystemExit) as e:
        console.onecmd('list groups')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_become_command(console):
    # Test toggling the become flag
    console.onecmd('become')
    assert hasattr(console, 'become'), "The 'become' attribute should be set"

def test_force_shell_module(console):
    # Test forcing shell module instead of Ansible module
    with pytest.raises(SystemExit) as e:
        console.onecmd('! yum update -y')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_verbosity_command(console):
    # Test setting verbosity level
    with pytest.raises(SystemExit) as e:
        console.onecmd('verbosity 2')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_forks_command(console):
    # Test setting number of forks
    with pytest.raises(SystemExit) as e:
        console.onecmd('forks 5')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_become_user_command(console):
    # Test setting become user
    with pytest.raises(SystemExit) as e:
        console.onecmd('become_user sudo')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_remote_user_command(console):
    # Test setting remote user
    with pytest.raises(SystemExit) as e:
        console.onecmd('remote_user admin')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_become_method_command(console):
    # Test setting privilege escalation method
    with pytest.raises(SystemExit) as e:
        console.onecmd('become_method sudo')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_check_mode_command(console):
    # Test toggling check mode
    with pytest.raises(SystemExit) as e:
        console.onecmd('check true')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_diff_mode_command(console):
    # Test toggling diff mode
    with pytest.raises(SystemExit) as e:
        console.onecmd('diff true')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_timeout_command(console):
    # Test setting timeout for tasks
    with pytest.raises(SystemExit) as e:
        console.onecmd('timeout 300')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_help_command(console):
    # Test displaying help for a specific command
    with pytest.raises(SystemExit) as e:
        console.onecmd('help cd')
    assert str(e.value) == '0'  # Ensure the command exits cleanly

def test_exit_command(console):
    # Test exiting the Ansible console
    with pytest.raises(SystemExit) as e:
        console.onecmd('exit')
    assert str(e.value) == '0'  # Ensure the command exits cleanly
