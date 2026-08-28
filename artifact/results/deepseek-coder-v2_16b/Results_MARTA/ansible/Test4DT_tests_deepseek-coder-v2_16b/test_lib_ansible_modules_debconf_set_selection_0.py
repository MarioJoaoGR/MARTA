
import pytest
from ansible.modules.debconf import set_selection

def test_set_boolean_value_for_unseen_package():
    class MockModule:
        def get_bin_path(self, bin_name, required):
            return 'mocked_path'
    
        def run_command(self, cmd, data=None):
            assert cmd == ['mocked_path', '-u']
            assert data == 'package_name question_id boolean true'
            return (0, "Success", "")
    
    module = MockModule()
    result = set_selection(module, 'package_name', 'question_id', 'boolean', 'True', True)
    assert result[0] == 0
    assert result[1] == "Success"

def test_set_string_value_for_package():
    class MockModule:
        def get_bin_path(self, bin_name, required):
            return 'mocked_path'
    
        def run_command(self, cmd, data=None):
            assert cmd == ['mocked_path']
            assert data == 'package_name question_id string some_value'
            return (0, "Success", "")
    
    module = MockModule()
    result = set_selection(module, 'package_name', 'question_id', 'string', 'some_value', False)
    assert result[0] == 0
    assert result[1] == "Success"
