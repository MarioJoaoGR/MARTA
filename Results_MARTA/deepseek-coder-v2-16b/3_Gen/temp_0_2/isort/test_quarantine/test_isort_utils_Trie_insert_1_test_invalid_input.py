
import pytest
from pathlib import Path
from typing import Any

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.nodes: dict[str, TrieNode] = {}
        self.config_info: tuple[str, dict[str, Any]] | None = (config_file, config_data) if config_data else None

class Trie:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.root: TrieNode = TrieNode(config_file, config_data)

    def insert(self, config_file: str, config_data: dict[str, Any]) -> None:
        resolved_config_path_as_tuple = Path(config_file).parent.resolve().parts

        temp = self.root

        for path in resolved_config_path_as_tuple:
            if path not in temp.nodes:
                temp.nodes[path] = TrieNode()

            temp = temp.nodes[path]

        temp.config_info = (config_file, config_data)

def test_invalid_input():
    trie = Trie()
    
    # Test with non-string path
    with pytest.raises(TypeError):
        trie.insert(12345, {"key": "value"})
    
    # Test with invalid data type for config_data
    with pytest.raises(TypeError):
        trie.insert("path/to/config", "not a dictionary")

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

isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        trie = Trie()
    
        # Test with non-string path
        with pytest.raises(TypeError):
            trie.insert(12345, {"key": "value"})
    
        # Test with invalid data type for config_data
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_invalid_input.py:36: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_utils_Trie_insert_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.07s ===============================
"""