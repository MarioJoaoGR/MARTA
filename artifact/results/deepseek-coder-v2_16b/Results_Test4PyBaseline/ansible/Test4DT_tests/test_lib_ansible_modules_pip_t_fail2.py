
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

# Test case to cover line 486: initializing an empty message string
def test_fail_initializes_empty_message(mock_module):
    _fail(mock_module, cmd="ls", out=None, err=None)
    assert mock_module.failed is True
    assert mock_module.cmd == "ls"
    assert mock_module.msg == ""

# Test case to cover line 487: adding stdout if it exists
def test_fail_adds_stdout(mock_module):
    _fail(mock_module, cmd="ls", out="Output of command", err=None)
    assert mock_module.failed is True
    assert mock_module.cmd == "ls"
    assert mock_module.msg == "stdout: Output of command"

# Test case to cover line 489: adding stderr if it exists
def test_fail_adds_stderr(mock_module):
    _fail(mock_module, cmd="ls", out=None, err="Error executing command")
    assert mock_module.failed is True
    assert mock_module.cmd == "ls"