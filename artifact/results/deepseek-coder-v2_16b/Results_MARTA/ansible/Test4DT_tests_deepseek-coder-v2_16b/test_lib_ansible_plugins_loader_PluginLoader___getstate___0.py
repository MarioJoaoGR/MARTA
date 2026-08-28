
import pytest
from ansible.plugins.loader import PluginLoader



def test_error_case():
    with pytest.raises(TypeError):
        config = [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
        loader = PluginLoader('MyClass', 'my_package', config, 'plugins', aliases={'Alias1': 'Class1', 'Alias2': 'Class2'})
        plugin = loader.get(None)  # Passing None should raise a TypeError