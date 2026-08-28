# Module: ansible.plugins.loader
# test_loader.py
from ansible.plugins.loader import Jinja2Loader
import pytest

@pytest.fixture
def loader():
    return Jinja2Loader()

def test_all_method(loader):
    plugins = loader.all()
    assert isinstance(plugins, list), "Expected a list of plugin files"
    assert len(plugins) > 0, "Expected at least one plugin file to be returned"
    for plugin in plugins:
        assert isinstance(plugin, str), f"Expected each item in the list to be a string (file path), but got {type(plugin)}"

def test_find_plugin_method(loader):
    try:
        plugin = loader.find_plugin('example_plugin', collection_list=['my_collection'])
        assert isinstance(plugin, str), f"Expected the found plugin to be a string (file path), but got {type(plugin)}"
    except Exception as e:
        pytest.fail(f"Unexpected error occurred while finding plugin: {e}")

def test_get_method(loader):
    try:
        plugin = loader.get('example_plugin', collection_list=['my_collection'])
        assert isinstance(plugin, str), f"Expected the retrieved plugin to be a string (file path), but got {type(plugin)}"
    except Exception as e:
        pytest.fail(f"Unexpected error occurred while retrieving plugin: {e}")
