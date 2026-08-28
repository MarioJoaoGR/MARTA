
import pytest
from httpie.plugins.manager import PluginManager

def test_plugin_manager_add_plugin():
    manager = PluginManager()
    class SomePluginClass: pass
    plugin1 = SomePluginClass()
    with pytest.raises(AttributeError):
        manager.add_plugin(plugin1)


def test_plugin_manager_filter():
    manager = PluginManager()
    class FormatterPlugin1: pass
    class FormatterPlugin2: pass
    with pytest.raises(AttributeError):
        manager.add_plugin(FormatterPlugin1())