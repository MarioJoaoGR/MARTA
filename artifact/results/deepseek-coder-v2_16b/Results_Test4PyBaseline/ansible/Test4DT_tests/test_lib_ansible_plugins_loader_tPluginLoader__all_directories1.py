
import pytest
import os
from ansible.plugins.loader import PluginLoader

# Test cases for _all_directories method
def test_all_directories_method():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    
    # Create a temporary directory structure for testing
    temp_dir = os.path.join(os.getcwd(), 'temp_test_dir')
    os.makedirs(os.path.join(temp_dir, 'subdir1', 'subdir2'), exist_ok=True)
    open(os.path.join(temp_dir, '__init__.py'), 'a').close()
    os.symlink('subdir1', os.path.join(temp_dir, 'symlinked_subdir'))
    
    dirs = loader._all_directories(temp_dir)
    assert isinstance(dirs, list)
    for dir in dirs:
        assert os.path.isabs(dir)
    
    # Clean up the temporary directory structure
    os.rmdir(os.path.join(temp_dir, 'subdir1', 'subdir2'))
    os.rmdir(os.path.join(temp_dir, 'subdir1'))
    os.remove(os.path.join(temp_dir, '__init__.py'))
    os.remove(os.path.join(temp_dir, 'symlinked_subdir'))
    os.rmdir(temp_dir)

def test_all_directories_method_with_symlinks():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    
    # Create a temporary directory structure for testing with symlinks
    temp_dir = os.path.join(os.getcwd(), 'temp_test_dir_symlinks')
    os.makedirs(os.path.join(temp_dir, 'subdir1', 'subdir2'), exist_ok=True)
    open(os.path.join(temp_dir, '__init__.py'), 'a').close()
    os.symlink('subdir1', os.path.join(temp_dir, 'symlinked_subdir'))
    
    dirs = loader._all_directories(temp_dir)
    assert isinstance(dirs, list)
    for dir in dirs:
        assert os.path.isabs(dir)
    
    # Check that the symlink itself is included and its target directory is also included
    assert any('symlinked_subdir' in d for d in dirs)
    assert any('subdir1' in d for d in dirs)
    
    # Clean up the temporary directory structure
    os.rmdir(os.path.join(temp_dir, 'subdir1', 'subdir2'))
    os.rmdir(os.path.join(temp_dir, 'subdir1'))
    os.remove(os.path.join(temp_dir, '__init__.py'))
    os.remove(os.path.join(temp_dir, 'symlinked_subdir'))
    os.rmdir(temp_dir)

def test_all_directories_method_with_no_symlinks():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    
    # Create a temporary directory structure for testing without symlinks
    temp_dir = os.path.join(os.getcwd(), 'temp_test_dir_no_symlinks')
    os.makedirs(os.path.join(temp_dir, 'subdir1', 'subdir2'), exist_ok=True)
    open(os.path.join(temp_dir, '__init__.py'), 'a').close()
    
    dirs = loader._all_directories(temp_dir)
    assert isinstance(dirs, list)
    for dir in dirs:
        assert os.path.isabs(dir)
    
    # Check that the symlink itself is not included and its target directory is also not included
    assert not any('symlinked_subdir' in d for d in dirs)
    assert any('subdir1' in d for d in dirs)
    
    # Clean up the temporary directory structure
    os.rmdir(os.path.join(temp_dir, 'subdir1', 'subdir2'))
    os.rmdir(os.path.join(temp_dir, 'subdir1'))
    os.remove(os.path.join(temp_dir, '__init__.py'))
    os.rmdir(temp_dir)
