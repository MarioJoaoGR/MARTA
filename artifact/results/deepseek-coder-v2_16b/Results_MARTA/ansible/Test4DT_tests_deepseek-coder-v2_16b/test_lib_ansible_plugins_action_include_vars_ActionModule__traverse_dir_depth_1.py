
import pytest
from ansible.plugins.action import include_vars
from pathlib import Path

# Assuming we have an instance of ActionModule named 'am' with a source_dir attribute set.
@pytest.fixture(scope="module")
def am():
    # Create a temporary directory for testing
    test_dir = Path("test_source_dir")
    test_dir.mkdir()
    
    # Add YAML and JSON files to the test directory
    (test_dir / "file1.yaml").touch()
    (test_dir / "file2.yml").touch()
    (test_dir / "file3.json").touch()
    
    am = include_vars._ActionModule(source_dir=str(test_dir))
    yield am
    # Clean up the temporary directory after the test
    for item in test_dir.iterdir():
        if item.is_file():
            item.unlink()
    test_dir.rmdir()

def test_valid_input_default_depth(am):
    am.depth = 0  # Unlimited depth
    generator = am._traverse_dir_depth()
    root_dirs, files_lists = zip(*generator)
    
    assert len(root_dirs) == 1  # Only one root directory expected
    assert list(files_lists[0]) == ['file1.yaml', 'file2.yml', 'file3.json']  # All files should be listed

def test_valid_input_specific_depth(am):
    am.depth = 3  # Specific depth limit of 3 levels
    generator = am._traverse_dir_depth()
    root_dirs, files_lists = zip(*generator)
    
    assert len(root_dirs) == 1  # Only one root directory expected
    assert list(files_lists[0]) == ['file1.yaml', 'file2.yml', 'file3.json']  # All files should be listed at the first level

def test_invalid_input_none():
    am = include_vars._ActionModule()
    with pytest.raises(TypeError):
        list(am._traverse_dir_depth())
