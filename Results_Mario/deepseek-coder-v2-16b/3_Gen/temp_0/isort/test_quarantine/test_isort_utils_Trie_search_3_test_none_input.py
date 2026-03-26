
import pytest
from pathlib import Path
from typing import Any, Dict

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.config_info = (config_file, config_data if config_data is not None else {})
        self.nodes: Dict[str, TrieNode] = {}

class Trie:
    def __init__(self, config_file: str = "", config_data: dict[str, Any] | None = None) -> None:
        self.root: TrieNode = TrieNode(config_file, config_data)

    def search(self, filename: str) -> tuple[str, dict[str, Any]]:
        resolved_file_path_as_tuple = Path(filename).resolve().parts

        temp = self.root

        last_stored_config: tuple[str, dict[str, Any]] = ("", {})

        for path in resolved_file_path_as_tuple:
            if temp.config_info[0]:
                last_stored_config = temp.config_info

            if path not in temp.nodes:
                break

            temp = temp.nodes[path]

        return last_stored_config

def test_none_input():
    trie = Trie()
    result = trie.search("non_existent_file")
    assert result == ()

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

isort/Test4DT_tests/test_isort_utils_Trie_search_3_test_none_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        trie = Trie()
        result = trie.search("non_existent_file")
>       assert result == ()
E       AssertionError: assert ('', {}) == ()
E         
E         Left contains 2 more items, first extra item: ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_utils_Trie_search_3_test_none_input.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_utils_Trie_search_3_test_none_input.py::test_none_input
============================== 1 failed in 0.10s ===============================
"""