# Module: ansible.module_utils.common.locale
import pytest
from ansible.module_utils.common.locale import get_best_parsable_locale
from unittest.mock import MagicMock

# Mock AnsibleModule for testing
class MockAnsibleModule:
    def __init__(self):
        self.params = {}
    
    def get_bin_path(self, tool):
        return "/usr/bin/locale" if tool == "locale" else None
    
    def run_command(self, command):
        if command[0] == "/usr/bin/locale" and command[1:] == ["-a"]:
            return 0, "C.utf8\nen_US.utf8\n", ""
        return 1, "", "Error occurred"

# Test cases for get_best_parsable_locale function
def test_get_best_parsable_locale_default_preferences():
    module = MockAnsibleModule()
    result = get_best_parsable_locale(module)
    assert result == 'C.utf8'

def test_get_best_parsable_locale_with_preferences():
    module = MockAnsibleModule()
    preferences = ['en_US.utf8', 'fr_FR.utf8']
    result = get_best_parsable_locale(module, preferences=preferences)
    assert result == 'en_US.utf8'

def test_get_best_parsable_locale_raise_on_locale():
    module = MockAnsibleModule()
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module, raise_on_locale=True)

def test_get_best_parsable_locale_with_invalid_command():
    module = MockAnsibleModule()
    module.run_command = MagicMock(return_value=(1, "", "Error occurred"))
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module)

def test_get_best_parsable_locale_with_invalid_output():
    module = MockAnsibleModule()
    module.run_command = MagicMock(return_value=(0, "", "Error occurred"))
    with pytest.raises(RuntimeWarning):
        get_best_parsable_locale(module)
