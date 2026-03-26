
import pytest
from pathlib import Path
from unittest.mock import MagicMock

class TrieNode:
    def __init__(self, config_file: str = "", config_data: dict | None = None) -> None:
        self.config_info = (config_file, config_data or {})
        self.nodes = {}

class Trie:
    """
    A prefix tree to store the paths of all config files and to search the nearest config associated with each file.
    
    Parameters:
        - `config_file`: A string representing the path to a configuration file. This parameter is optional and defaults to an empty string if not provided.
        - `config_data`: A dictionary containing configuration data. This parameter is optional and defaults to None if not provided. If provided, it should be a dictionary mapping strings to any type of values.
    
    Configures the trie with the given configuration file or data. The class supports two initialization methods:
    1. Without arguments (default values for both `config_file` and `config_data`), which initializes an empty Trie.
    2. With a `config_file` and/or `config_data`, which uses the provided configuration file or data to initialize the root node of the trie.
    
    Example usage:
        # Creating an instance with default values
        trie = Trie()
        
        # Creating an instance with specific configuration file and data
        trie = Trie(config_file="path/to/config", config_data={"key": "value"})
    """
    def __init__(self, config_file: str = "", config_data: dict | None = None) -> None:
        self.root: TrieNode = TrieNode(config_file, config_data)

    def search(self, filename: str) -> tuple[str, dict]:
        """
        Returns the closest config relative to filename by doing a depth first search on the prefix tree.
        
        Parameters:
            filename (str): The path of the file for which to find the closest configuration.
            
        Returns:
            tuple[str, dict]: A tuple containing the name of the closest configuration and its dictionary representation. If no configuration is found, it returns an empty tuple.
        """
        resolved_file_path_as_tuple = Path(filename).resolve().parts

        temp = self.root

        last_stored_config: tuple[str, dict] = ("", {})

        for path in resolved_file_path_as_tuple:
            if temp.config_info[0]:
                last_stored_config = temp.config_info

            if path not in temp.nodes:
                break

            temp = temp.nodes[path]

        return last_stored_config

@pytest.fixture(scope="module")
def trie():
    # Create a mock Trie instance for testing
    return Trie()

def test_invalid_input(trie):
    # Test invalid filename that does not exist in the trie structure, expecting an empty tuple as output
    assert trie.search("nonexistentfile") == ("", {})
