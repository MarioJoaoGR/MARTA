
import pytest
from shell_module import ShellModule

# Create an instance of ShellModule for PowerShell
@pytest.fixture(scope="function")
def shell_module():
    return ShellModule()

# Test scenario 1: Valid input happy path
def test_valid_input_happy_path(shell_module):
    # Test a valid path with trailing slash
    assert shell_module.path_has_trailing_slash("C:/path/to/file/") == True
    # Test a valid path without trailing slash
    assert shell_module.path_has_trailing_slash("C:/path/to/file") == False
    # Test another valid Windows path with trailing slash
    assert shell_module.path_has_trailing_slash("C:\\path\\to\\file\\") == True
    # Test another valid Windows path without trailing slash
    assert shell_module.path_has_trailing_slash("C:\\path\\to\\file") == False

# Test scenario 2: Edge cases
def test_edge_cases(shell_module):
    # Test None input
    with pytest.raises(TypeError):
        shell_module.path_has_trailing_slash(None)
    # Test empty string
    assert shell_module.path_has_trailing_slash("") == False
    # Test path without trailing slash
    assert shell_module.path_has_trailing_slash("C:/path/to/file") == False
    # Test another path without trailing slash
    assert shell_module.path_has_trailing_slash("C:\\path\\to\\file") == False

# Test scenario 3: Invalid inputs
def test_invalid_inputs(shell_module):
    # Test invalid type (int)
    with pytest.raises(AttributeError):
        shell_module.path_has_trailing_slash(12345)
    # Test invalid type (list)
    with pytest.raises(AttributeError):
        shell_module.path_has_trailing_slash([1, 2, 3])
    # Test invalid type (dict)
    with pytest.raises(AttributeError):
        shell_module.path_has_trailing_slash({})
