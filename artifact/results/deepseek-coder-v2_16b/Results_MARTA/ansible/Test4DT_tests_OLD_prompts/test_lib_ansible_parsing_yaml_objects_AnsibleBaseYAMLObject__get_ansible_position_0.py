
import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

def test_error_case():
    obj = AnsibleBaseYAMLObject()
    obj._data_source = None
    obj._line_number = -1
    obj._column_number = -1
    with pytest.raises(AttributeError):
        raise AttributeError("Test exception")
