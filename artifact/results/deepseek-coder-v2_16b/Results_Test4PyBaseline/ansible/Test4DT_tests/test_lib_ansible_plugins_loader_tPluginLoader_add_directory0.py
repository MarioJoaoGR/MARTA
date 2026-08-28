# Module: ansible.plugins.loader
import pytest
from ansible.plugins.loader import PluginLoader
import os

# Fixture for creating a PluginLoader instance with default parameters
@pytest.fixture
def plugin_loader():
    return PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')

# Test case to check if the PluginLoader can be instantiated correctly
def test_plugin_loader_instantiation(plugin_loader):
    assert isinstance(plugin_loader, PluginLoader)

# Test case to add a directory and verify it is added to the search path
def test_add_directory(plugin_loader):
    initial_extra_dirs = plugin_loader._extra_dirs.copy()
    new_directory = '/new/directory'
    plugin_loader.add_directory(new_directory, with_subdir=True)
    assert new_directory in plugin_loader._extra_dirs
    assert len(plugin_loader._extra_dirs) == len(initial_extra_dirs) + 1

# Test case to add a directory without subdir and verify it is added to the search path
def test_add_directory_without_subdir(plugin_loader):
    initial_extra_dirs = plugin_loader._extra_dirs.copy()
    new_directory = '/new/directory'
    plugin_loader.add_directory(new_directory, with_subdir=False)
    assert new_directory in plugin_loader._extra_dirs
    assert len(plugin_loader._extra_dirs) == len(initial_extra_dirs) + 1

# Test case to add an already added directory and verify it does not increase the count
def test_add_existing_directory(plugin_loader):
    initial_extra_dirs = plugin_loader._extra_dirs.copy()
    existing_directory = '/path/to/config'
    plugin_loader.add_directory(existing_directory, with_subdir=True)
    assert len(plugin_loader._extra_dirs) == len(initial_extra_dirs)

# Test case to add a directory with invalid path and verify it does not affect the search path
def test_add_invalid_directory():
    plugin_loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    initial_extra_dirs = plugin_loader._extra_dirs.copy()
    invalid_directory = '/nonexistent/directory'
    plugin_loader.add_directory(invalid_directory, with_subdir=True)
    assert len(plugin_loader._extra_dirs) == len(initial_extra_dirs)
