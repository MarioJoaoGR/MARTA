
import pytest
from unittest.mock import patch
from os import path

class ActionModule:
    TRANSFERS_FILES = False
    VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
    VALID_DIR_ARGUMENTS = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    VALID_FILE_ARGUMENTS = ['file', '_raw_params']
    VALID_ALL = ['name', 'hash_behaviour']

    def _is_valid_file_ext(self, source_file):
        """ Verify if source file has a valid extension
        
        This function checks whether the provided `source_file` has a valid file extension. It supports checking for '.yaml', '.yml', and '.json' extensions.
        
        Args:
            source_file (str): The full path of the source file or just the filename if it is in the current directory.
            
        Returns:
            bool: True if the file extension is valid, False otherwise.
        
        Example:
            >>> am = ActionModule()
            >>> print(am._is_valid_file_ext('example.yaml'))  # Output: True
            >>> print(am._is_valid_file_ext('example.txt'))   # Output: False
        """
        file_ext = path.splitext(source_file)
        return bool(len(file_ext) > 1 and file_ext[-1][1:] in self.VALID_FILE_EXTENSIONS)

# Test cases for ActionModule class
@pytest.fixture
def am():
    return ActionModule()

def test_valid_extension(am):
    assert am._is_valid_file_ext('example.yaml') == True
    assert am._is_valid_file_ext('example.yml') == True
    assert am._is_valid_file_ext('example.json') == True

def test_invalid_extension(am):
    assert am._is_valid_file_ext('example.txt') == False
    assert am._is_valid_file_ext('example.log') == False

def test_none_input(am):
    with pytest.raises(TypeError):
        am._is_valid_file_ext(None)
