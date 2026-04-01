
import pytest
from isort.utils import Trie, TrieNode
from pathlib import Path

def test_edge_case_none():
    trie = Trie()
    assert isinstance(trie.root, TrieNode)
    assert not trie.root.nodes
    assert trie.root.config_info is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        trie = Trie()
        assert isinstance(trie.root, TrieNode)
        assert not trie.root.nodes
>       assert trie.root.config_info is None
E       AssertionError: assert ('', {}) is None
E        +  where ('', {}) = <isort.utils.TrieNode object at 0x7f1183f42850>.config_info
E        +    where <isort.utils.TrieNode object at 0x7f1183f42850> = <isort.utils.Trie object at 0x7f1183f42390>.root

isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_edge_case_none.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.12s ===============================
"""