
import pytest
from isort.utils import TrieNode

def test_edge_cases():
    # Test with only config_file provided
    trie_node_with_file = TrieNode(config_file="test.cfg")
    assert trie_node_with_file.config_info == ("test.cfg", {})
    
    # Test with only config_data provided
    trie_node_with_data = TrieNode(config_data={"key": "value"})
    assert trie_node_with_data.config_info == ("", {"key": "value"})
    
    # Test with both config_file and config_data provided (should ignore config_file)
    trie_node_both = TrieNode(config_file="test.cfg", config_data={"key": "value"})
    assert trie_node_both.config_info == ("", {"key": "value"})

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

isort/Test4DT_tests/test_isort_utils_TrieNode___init___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with only config_file provided
        trie_node_with_file = TrieNode(config_file="test.cfg")
        assert trie_node_with_file.config_info == ("test.cfg", {})
    
        # Test with only config_data provided
        trie_node_with_data = TrieNode(config_data={"key": "value"})
        assert trie_node_with_data.config_info == ("", {"key": "value"})
    
        # Test with both config_file and config_data provided (should ignore config_file)
        trie_node_both = TrieNode(config_file="test.cfg", config_data={"key": "value"})
>       assert trie_node_both.config_info == ("", {"key": "value"})
E       AssertionError: assert ('test.cfg', {'key': 'value'}) == ('', {'key': 'value'})
E         
E         At index 0 diff: 'test.cfg' != ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_utils_TrieNode___init___1_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_utils_TrieNode___init___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""