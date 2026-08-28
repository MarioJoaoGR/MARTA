
import pytest
from thefuck.shells.generic import Generic

# Assuming SpecificShell is a subclass of Generic with _get_version implemented
class SpecificShell(Generic):
    def _get_version(self):
        return '1.0'  # Example version string

def test_info_with_version():
    specific_shell = SpecificShell()
    assert specific_shell.info() == 'Generic Shell 1.0'

def test_info_without_version():
    class NoVersionShell(Generic):
        friendly_name = 'No Version Shell'
        def _get_version(self):
            raise NotImplementedError("This method should not be called")
    
    no_version_shell = NoVersionShell()