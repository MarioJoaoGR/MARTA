
import os
from pytutils.path import join_each

def test_edge_case_none():
    parent = "parent_dir"
    iterable = ["child1", "child2"]
    
    expected_output = ['parent_dir/child1', 'parent_dir/child2']
    actual_output = list(join_each(parent, iterable))
    
    assert actual_output == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""