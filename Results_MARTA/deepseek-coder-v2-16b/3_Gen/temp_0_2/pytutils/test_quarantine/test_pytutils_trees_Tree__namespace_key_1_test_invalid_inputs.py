
import pytest
from pytutils.trees import Tree

def test_invalid_inputs():
    with pytest.raises(TypeError):
        tree = Tree(initial='not a dictionary')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_trees_Tree__namespace_key_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
>           tree = Tree(initial='not a dictionary')

pytutils/Test4DT_tests/test_pytutils_trees_Tree__namespace_key_1_test_invalid_inputs.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Tree(<class 'pytutils.trees.Tree'>, {}), initial = 'not a dictionary'
namespace = '', initial_is_ref = False

    def __init__(self, initial=None, namespace='', initial_is_ref=False):
        if initial is not None and initial_is_ref:
            self.data = initial_is_ref
        self.namespace = namespace
        super(Tree, self).__init__(self.__class__)
        if initial is not None:
>           self.update(initial)
E           ValueError: dictionary update sequence element #0 has length 1; 2 is required

pytutils/pytutils/trees.py:78: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_Tree__namespace_key_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""