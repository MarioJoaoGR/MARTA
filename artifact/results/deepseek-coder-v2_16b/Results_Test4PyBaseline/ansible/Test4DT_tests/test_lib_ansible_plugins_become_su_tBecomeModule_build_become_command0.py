# Module: ansible.plugins.become.su
import pytest
from ansible.plugins.become import su

# Initialize the su module
su_module = su.BecomeModule()

@pytest.mark.parametrize("cmd, shell, expected", [
    ("ls -l", True, "su ls -l"),  # Test with a simple command and shell=True
    ("ipconfig", True, "su ipconfig"),  # Test with another simple command and shell=True
    ("echo 'hello'", False, "su -c 'echo \"hello\"'"),  # Test with a complex command and shell=False
    (None, False, None),  # Test with no command and shell=False
])
def test_build_become_command(cmd, shell, expected):
    result = su_module.build_become_command(cmd, shell)
    assert result == expected
