# Module: thefuck.shells.generic
# test_generic.py
from thefuck.shells.generic import Generic

def test_to_shell():
    generic_instance = Generic()
    command_script = 'ls -l'
    prepared_command = generic_instance.to_shell(command_script)
    assert prepared_command == 'ls -l', f"Expected 'ls -l' but got {prepared_command}"
