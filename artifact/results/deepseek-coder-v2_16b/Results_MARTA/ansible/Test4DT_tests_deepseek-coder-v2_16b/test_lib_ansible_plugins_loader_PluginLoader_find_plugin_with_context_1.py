
import pytest
from ansible.plugins.loader import PluginLoader
import os

@pytest.fixture(scope="module")
def loader():
    return PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')


def test_edge_case(loader):
    with pytest.raises(TypeError) as excinfo:
        context = loader.find_plugin_with_context(None)
    assert 'expected str, bytes or os.PathLike object' in str(excinfo.value), "Expected TypeError but got a different error"
