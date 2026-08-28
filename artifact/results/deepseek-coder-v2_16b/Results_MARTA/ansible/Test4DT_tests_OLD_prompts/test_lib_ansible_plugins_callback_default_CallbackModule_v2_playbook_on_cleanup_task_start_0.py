
import pytest
from unittest.mock import patch
from ansible.plugins.callback.default import CallbackModule

def test_v2_playbook_on_cleanup_task_start():
    with patch('ansible.plugins.callback.default.CallbackModule.__init__', return_value=None):
        callback = CallbackModule()
        task = {'uuid': 'test_uuid'}  # Mocking a task dictionary
        
        with pytest.raises(AttributeError) as excinfo:
            callback.v2_playbook_on_cleanup_task_start(task)
    
    assert str(excinfo.value) == "'CallbackModule' object has no attribute '_task_type_cache'"
