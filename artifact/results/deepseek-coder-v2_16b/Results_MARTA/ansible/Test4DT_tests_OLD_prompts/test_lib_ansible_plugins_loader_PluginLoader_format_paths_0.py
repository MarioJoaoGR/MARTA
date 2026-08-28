
import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoader, MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE
from collections import defaultdict
import os

class BasePluginClass:
    pass



def test_format_paths():
    loader = PluginLoader('ClassName', 'PackageName', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    paths_to_format = ['/usr/lib', '/usr/local/lib', '/usr/lib']
    formatted_paths = loader.format_paths(paths_to_format)
    assert formatted_paths == os.pathsep.join(['/usr/lib', '/usr/local/lib'])