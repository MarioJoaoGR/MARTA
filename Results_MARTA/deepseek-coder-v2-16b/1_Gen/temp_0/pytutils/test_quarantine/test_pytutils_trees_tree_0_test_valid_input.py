
import pytest
import collections
from pytutils.trees import tree

@pytest.fixture
def nested_tree():
    return tree()

def test_valid_input(nested_tree):
    assert isinstance(nested_tree, collections.defaultdict)
    assert isinstance(nested_tree['key'], collections.defaultdict)
    assert len(nested_tree) == 0

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

pytutils/Test4DT_tests/test_pytutils_trees_tree_0_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

nested_tree = defaultdict(<function tree at 0x7fa77bced620>, {'key': defaultdict(<function tree at 0x7fa77bced620>, {})})

    def test_valid_input(nested_tree):
        assert isinstance(nested_tree, collections.defaultdict)
        assert isinstance(nested_tree['key'], collections.defaultdict)
>       assert len(nested_tree) == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = len(defaultdict(<function tree at 0x7fa77bced620>, {'key': defaultdict(<function tree at 0x7fa77bced620>, {})}))

pytutils/Test4DT_tests/test_pytutils_trees_tree_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_trees_tree_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""