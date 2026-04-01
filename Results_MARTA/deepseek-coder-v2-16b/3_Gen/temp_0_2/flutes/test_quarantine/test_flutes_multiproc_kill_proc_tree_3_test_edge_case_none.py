
import pytest
from flutes.multiproc import kill_proc_tree
import psutil
import os
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code before each test
    yield  # This is where the testing happens
    # Teardown code after each test

@patch('flutes.multiproc.psutil')
def test_kill_proc_tree(mock_psutil):
    mock_parent = MagicMock()
    mock_children = [MagicMock(), MagicMock()]
    
    mock_psutil.Process.return_value = mock_parent
    mock_parent.children.return_value = mock_children
    
    kill_proc_tree(os.getpid())
    
    assert mock_parent.kill.call_count == 1
    for child in mock_children:
        assert child.kill.called
    assert mock_psutil.wait_procs.called

@patch('flutes.multiproc.psutil')
def test_kill_proc_tree_including_parent(mock_psutil):
    mock_parent = MagicMock()
    mock_children = [MagicMock(), MagicMock()]
    
    mock_psutil.Process.return_value = mock_parent
    mock_parent.children.return_value = mock_children
    
    kill_proc_tree(os.getpid(), including_parent=True)
    
    assert mock_parent.kill.call_count == 1
    for child in mock_children:
        assert child.kill.called
    assert mock_psutil.wait_procs.called
    assert mock_parent.kill.call_count == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_case_none.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_kill_proc_tree ______________________________

args = (), keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/usr/local/lib/python3.11/unittest/mock.py:1375: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:137: in __enter__
    return next(self.gen)
/usr/local/lib/python3.11/unittest/mock.py:1357: in decoration_helper
    arg = exit_stack.enter_context(patching)
/usr/local/lib/python3.11/contextlib.py:517: in enter_context
    result = _enter(cm)
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f039c01c4d0>

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
_____________________ test_kill_proc_tree_including_parent _____________________

args = (), keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/usr/local/lib/python3.11/unittest/mock.py:1375: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:137: in __enter__
    return next(self.gen)
/usr/local/lib/python3.11/unittest/mock.py:1357: in decoration_helper
    arg = exit_stack.enter_context(patching)
/usr/local/lib/python3.11/contextlib.py:517: in enter_context
    result = _enter(cm)
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f039bec1510>

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
FAILED flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_case_none.py::test_kill_proc_tree
FAILED flutes/Test4DT_tests/test_flutes_multiproc_kill_proc_tree_3_test_edge_case_none.py::test_kill_proc_tree_including_parent
============================== 2 failed in 0.28s ===============================
"""