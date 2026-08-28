
import pytest
from ansible.plugins.loader import PluginLoader

# Test scenarios
def test_valid_inputs():
    # Arrange
    class_name = 'MyClass'
    package = 'my_package'
    config = ['/path/to/config1']
    subdir = 'plugins'
    
    # Act
    loader = PluginLoader(class_name, package, config, subdir)
    
    # Assert
    assert loader.class_name == class_name
    assert loader.package == package
    assert loader.config == config
    assert loader.subdir == subdir

def test_edge_cases():
    # Arrange
    class_name = None
    package = None
    config = []
    subdir = ''
    
    # Act
    with pytest.raises(TypeError):  # PluginLoader should raise a TypeError for invalid inputs
        loader = PluginLoader(class_name, package, config, subdir)
    
    # Assert is handled by the exception being raised

def test_invalid_inputs():
    # Arrange/Act/Assert are all handled by pytest.raises which will fail if no exception is raised
    with pytest.raises(TypeError):  # PluginLoader should raise a TypeError for invalid inputs
        loader = PluginLoader()
