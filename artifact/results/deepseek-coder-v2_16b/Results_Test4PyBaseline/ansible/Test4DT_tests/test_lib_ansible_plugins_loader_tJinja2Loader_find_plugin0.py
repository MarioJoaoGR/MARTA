# Module: ansible.plugins.loader
import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader

# Fixture to create an instance of the Jinja2Loader class for testing
@pytest.fixture(scope="module")
def loader():
    return Jinja2Loader()

# Test case for finding a specific plugin with a fully qualified collection reference (FQCR)
def test_find_plugin_with_fqcr(loader):
    name = "example_plugin.my_collection"
    collection_list = ['my_collection']
    with pytest.raises(AnsibleError) as excinfo:
        loader.find_plugin(name, collection_list=collection_list)
    assert str(excinfo.value) == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'

# Test case for finding a specific plugin without an FQCR
def test_find_plugin_without_fqcr(loader):
    name = "example_plugin"
    collection_list = ['my_collection']
    with pytest.raises(AnsibleError) as excinfo:
        loader.find_plugin(name, collection_list=collection_list)
    assert str(excinfo.value) == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'

# Test case to ensure the all method raises an error as it is not implemented
def test_all_method(loader):
    with pytest.raises(AnsibleError) as excinfo:
        loader.all()
    assert str(excinfo.value) == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'
