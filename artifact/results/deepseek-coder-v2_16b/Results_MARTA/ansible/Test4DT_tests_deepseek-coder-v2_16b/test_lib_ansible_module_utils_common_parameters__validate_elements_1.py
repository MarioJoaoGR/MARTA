
import pytest
from ansible.module_utils.common.parameters import _validate_elements, AnsibleValidationErrorMultiple, ElementError
from ansible.errors import AnsibleError

def test_validate_elements_with_builtin_type():
    values = [1, 'string', 3.14]
    validated_values = _validate_elements('int', 'numbers', values)
    assert len(validated_values) == 1 and isinstance(validated_values[0], int)




def test_validate_elements_with_none_wanted_type():
    values = [1, 'string', 3.14]
    validated_values = _validate_elements(None, 'numbers', values)
    assert len(validated_values) == 3 and all(isinstance(v, (int, str)) for v in validated_values)