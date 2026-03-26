
import pytest

from isort.utils import TrieNode


@pytest.fixture(scope="module")
def trie_node():
    return TrieNode()

def test_valid_inputs(trie_node):
    # Test creating a TrieNode with both config_file and config_data provided
    config_file = "path/to/config"
    config_data = {"key": "value"}
    trie_node_with_args = TrieNode(config_file=config_file, config_data=config_data)
    
    # Check if the config_info attribute is correctly set
    assert trie_node_with_args.config_info == (config_file, config_data)
    
    # Test creating a TrieNode with only config_file provided
    trie_node_only_file = TrieNode(config_file=config_file)
    assert trie_node_only_file.config_info == (config_file, {})
    
    # Test creating a TrieNode with only config_data provided
    trie_node_only_data = TrieNode(config_data=config_data)
    assert trie_node_only_data.config_info == ("", config_data)
    
    # Test creating a TrieNode without any arguments
    trie_node_no_args = TrieNode()
    assert trie_node_no_args.config_info == ("", {})
