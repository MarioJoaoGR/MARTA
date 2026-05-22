
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.mark.skipif(not hasattr(Path, "mkdir"), reason="requires os.mkdir to be mocked")
def test_invalid_inputs():
    env = MagicMock()
    env.config.plugins_dir = Path('/invalid/path')
    
    with patch('os.mkdir', side_effect=OSError):
        with pytest.raises(OSError):
            installer = PluginInstaller(env=env, debug=False)
