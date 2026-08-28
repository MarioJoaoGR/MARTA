
import os
from pathlib import Path
import pytest
from apimd.loader import walk_packages

# Define constants for testing
TEST_ROOT = Path("/tmp/test_apimd_loader_walk_packages")
mypackage_path = TEST_ROOT / "mypackage"
subpackage_path = mypackage_path / "subpackage"

@pytest.fixture(scope="module", autouse=True)
def setup_test_directory():
    # Create the test directory structure
    os.makedirs(subpackage_path, exist_ok=True)

    # Create test files
    (mypackage_path / "__init__.py").touch()
    (mypackage_path / "module1.py").touch()
    (subpackage_path / "__init__.py").touch()
    (subpackage_path / "module2.py").touch()




def test_nonexistent_package():
    # Test a package that does not exist
    result = list(walk_packages('nonexistentpackage', str(TEST_ROOT)))
    assert result == []

