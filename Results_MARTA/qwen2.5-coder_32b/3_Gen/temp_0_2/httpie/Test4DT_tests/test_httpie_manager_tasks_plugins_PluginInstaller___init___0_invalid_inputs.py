
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.manager.tasks.plugins import PluginInstaller

def test_invalid_inputs():
    env = MagicMock()
    env.config.plugins_dir = Path('/invalid/path')
    
    with patch('os.mkdir', side_effect=OSError):
        with pytest.raises(OSError):
            installer = PluginInstaller(env=env, debug=False)
