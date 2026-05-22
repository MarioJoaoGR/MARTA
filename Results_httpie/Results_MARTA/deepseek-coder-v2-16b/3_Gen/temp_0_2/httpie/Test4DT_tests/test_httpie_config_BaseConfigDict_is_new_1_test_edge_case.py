
from pathlib import Path
from unittest.mock import patch
import httpie.config

class BaseConfigDict:
    """
    A base class for configuration dictionaries, providing basic functionality to check if a config file exists.

    Parameters:
        path (Path): The path to the configuration file. This parameter is required and must be an instance of the Path class from the standard library's 'pathlib' module.

    Attributes:
        path (Path): The path to the configuration file, initialized in the constructor.

    Methods:
        is_new(): Checks if the config file exists at the specified path. Returns True if the file does not exist, and False otherwise.

    Examples:
        To create a BaseConfigDict instance for a specific configuration file:
        
        ```python
        from pathlib import Path
        base_config = BaseConfigDict(Path('/path/to/config/file'))
        ```

        To check if the config file is new (i.e., does not exist):
        
        ```python
        if base_config.is_new():
            print("The configuration file has not been created yet.")
        else:
            print("The configuration file already exists.")
        ```
    
    The `is_new` method is intended to determine whether a new configuration object is needed for the HTTPie CLI tool, returning True if the configuration file does not exist and False otherwise. This functionality aligns with the broader goal of ensuring that the appropriate initialization steps are taken when using the BaseConfigDict class within the context of the HTTPie CLI tool's configuration management.
    """
    def __init__(self, path: Path):
        self.path = path

    def is_new(self) -> bool:
        return not self.path.exists()

def test_edge_case():
    with patch('httpie.config.BaseConfigDict.__init__', return_value=None):
        config = BaseConfigDict(path=Path('/some/file/path'))
        assert config.is_new() is True
