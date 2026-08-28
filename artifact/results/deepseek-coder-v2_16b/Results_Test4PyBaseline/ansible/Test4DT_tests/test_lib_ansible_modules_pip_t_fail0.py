
import pytest
from ansible.modules.pip import _fail

@pytest.fixture
def mock_module():
    class MockModule:
        def __init__(self):
            self.failed = False
            self.cmd = None
            self.msg = None
        
        def fail_json(self, cmd=None, msg=None):
            self.failed = True
            self.cmd = cmd
            self.msg = msg
    
    return MockModule()

def test_fail_basic_usage(mock_module):
    _fail(mock_module, cmd="ls", out=None, err="Error executing command")
    assert mock_module.failed is True
    assert mock_module.cmd == "ls"