
import os
from unittest.mock import patch, MagicMock
import pytest
from flutes.multiproc import kill_proc_tree

@pytest.fixture(autouse=True)
def mock_psutil():
    with patch('flutes.multiproc.psutil') as mock_psutil:
        yield mock_psutil

def test_kill_proc_tree_valid_inputs():
    # Mock psutil.Process to return a mock object
    mock_process = MagicMock()
    mock_children = [MagicMock(), MagicMock()]
    mock_process.children.return_value = mock_children
    
    # Set up the mock for psutil.Process
    with patch('flutes.multiproc.psutil.Process', return_value=mock_process):
        pid = os.getpid()
        kill_proc_tree(pid)
        
        # Check if children processes are killed
        assert mock_children[0].kill.called
        assert mock_children[1].kill.called
        
        # Check if the parent process is also terminated if including_parent=True
        assert mock_process.kill.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
______________ ERROR at setup of test_kill_proc_tree_valid_inputs ______________

    @pytest.fixture(autouse=True)
    def mock_psutil():
>       with patch('flutes.multiproc.psutil') as mock_psutil:

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_valid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f417923d550>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'flutes.multiproc' from '/projects/F202407648IACDCF2/mario/flutes/flutes/multiproc.py'> does not have the attribute 'psutil'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_valid_inputs.py::test_kill_proc_tree_valid_inputs
=============================== 1 error in 0.16s ===============================
"""