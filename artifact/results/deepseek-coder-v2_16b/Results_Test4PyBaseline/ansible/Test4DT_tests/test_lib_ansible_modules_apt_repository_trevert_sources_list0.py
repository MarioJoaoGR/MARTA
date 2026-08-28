# Module: ansible.modules.apt_repository
import pytest
import os
from your_module import revert_sources_list

# Define a fixture for creating temporary source directories and files
@pytest.fixture(scope="function")
def temp_source_dir():
    # Create temporary directory for sources
    temp_dir = "temp_source_dir"
    os.makedirs(temp_dir, exist_ok=True)
    
    yield temp_dir
    
    # Clean up the temporary directory after test
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(temp_dir)

def test_revert_sources_list_basic(temp_source_dir):
    # Create initial source list before modifications
    sources_before = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "content2"
    }
    with open(sources_before["file1"], "w") as f:
        f.write("content1")
    with open(sources_before["file2"], "w") as f:
        f.write("content2")
    
    # Modify the source list after modifications
    sources_after = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "modified_content",
        os.path.join(temp_source_dir, "new_file"): "new_content"
    }
    with open(sources_after["file2"], "w") as f:
        f.write("modified_content")
    with open(sources_after["new_file"], "w") as f:
        f.write("new_content")
    
    # Save the initial state of the source list
    sourceslist_before = None  # Assuming this is an object that can save the original state
    
    revert_sources_list(sources_before, sources_after, sourceslist_before)
    
    # Check if the new file has been removed and the existing files have been reverted to their original content
    assert not os.path.exists(sources_after["new_file"])
    with open(sources_before["file1"], "r") as f:
        assert f.read() == "content1"
    with open(sources_before["file2"], "r") as f:
        assert f.read() == "content2"

def test_revert_sources_list_empty_modifications(temp_source_dir):
    # Create initial source list before modifications
    sources_before = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "content2"
    }
    with open(sources_before["file1"], "w") as f:
        f.write("content1")
    with open(sources_before["file2"], "w") as f:
        f.write("content2")
    
    # No modifications after changes
    sources_after = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "modified_content"
    }
    with open(sources_after["file2"], "w") as f:
        f.write("modified_content")
    
    # Save the initial state of the source list
    sourceslist_before = None  # Assuming this is an object that can save the original state
    
    revert_sources_list(sources_before, sources_after, sourceslist_before)
    
    # Check if the file has been reverted to its original content
    with open(sources_before["file1"], "r") as f:
        assert f.read() == "content1"
    with open(sources_before["file2"], "r") as f:
        assert f.read() == "content2"

def test_revert_sources_list_nonexistent_files(temp_source_dir):
    # Create initial source list before modifications
    sources_before = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "content2"
    }
    with open(sources_before["file1"], "w") as f:
        f.write("content1")
    with open(sources_before["file2"], "w") as f:
        f.write("content2")
    
    # Modify the source list after modifications, adding a new file that does not exist initially
    sources_after = {
        os.path.join(temp_source_dir, "file1"): "content1",
        os.path.join(temp_source_dir, "file2"): "modified_content",
        os.path.join(temp_source_dir, "new_file"): "new_content"
    }
    with open(sources_after["file2"], "w") as f:
        f.write("modified_content")
    
    # Save the initial state of the source list
    sourceslist_before = None  # Assuming this is an object that can save the original state
    
    revert_sources_list(sources_before, sources_after, sourceslist_before)
    
    # Check if the new file has been removed and the existing files have been reverted to their original content
    assert not os.path.exists(sources_after["new_file"])
    with open(sources_before["file1"], "r") as f:
        assert f.read() == "content1"
    with open(sources_before["file2"], "r") as f:
        assert f.read() == "content2"
