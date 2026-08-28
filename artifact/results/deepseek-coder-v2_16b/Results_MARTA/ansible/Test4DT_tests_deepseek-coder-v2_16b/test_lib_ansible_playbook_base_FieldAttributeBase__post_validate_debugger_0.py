
import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError

# Test valid debugger value
def test_valid_debugger_value():
    field = FieldAttributeBase()
    field._post_validate_debugger("debugger", "always", None)  # Assuming templar is not needed for this validation
    assert True, "Test should pass as the debugger value is valid"

# Test invalid debugger value raises error
def test_invalid_debugger_value():
    field = FieldAttributeBase()
    with pytest.raises(AnsibleParserError) as excinfo:
        field._post_validate_debugger("debugger", "invalid_value", None)  # Assuming templar is not needed for this validation
    assert str(excinfo.value) == "'invalid_value' is not a valid value for debugger. Must be one of always, on_failed, on_unreachable, on_skipped, never"

# Test missing debugger value raises error
def test_missing_debugger_value():
    field = FieldAttributeBase()
    with pytest.raises(AnsibleParserError) as excinfo:
        field._post_validate_debugger("debugger", None, None)  # Assuming templar is not needed for this validation
    assert str(excinfo.value) == "'None' is not a valid value for debugger. Must be one of always, on_failed, on_unreachable, on_skipped, never"
