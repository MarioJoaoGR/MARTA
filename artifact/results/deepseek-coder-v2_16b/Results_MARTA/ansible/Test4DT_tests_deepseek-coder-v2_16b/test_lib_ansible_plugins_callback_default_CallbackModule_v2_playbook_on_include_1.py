
import pytest
from ansible.plugins.callback.default import CallbackModule



def test_valid_input():
    cb = CallbackModule()
    included_file = {
        '_filename': 'additional_tasks.yml',
        '_hosts': [{'name': 'host1'}, {'name': 'host2'}],
        '_vars': {}
    }
    
    with pytest.raises(AttributeError):  # Since _filename is not defined in the provided input type, this should raise an AttributeError
        cb.v2_playbook_on_include(included_file)