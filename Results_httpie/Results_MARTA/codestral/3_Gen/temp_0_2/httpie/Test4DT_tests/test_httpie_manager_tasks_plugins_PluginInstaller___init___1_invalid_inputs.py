
import pytest
from unittest.mock import patch, MagicMock
from os import mkdir
from pathlib import Path

class Environment:
    def __init__(self):
        self.config = MagicMock()
        self.config.plugins_dir = Path("/invalid/path")

class PluginInstaller:
    def __init__(self, env: Environment, debug: bool = False) -> None:
        self.env = env
        self.dir = env.config.plugins_dir
        self.debug = debug

    def setup_plugins_dir(self):
        try:
            mkdir(str(self.dir))
        except OSError as e:
            print(f"Error creating directory: {e}")
            raise OSError from e

@pytest.fixture
def env():
    return Environment()

@pytest.mark.skipif(not hasattr(Path, "mkdir"), reason="requires os.mkdir")
def test_invalid_inputs(env):
    with patch('os.mkdir', side_effect=OSError):
        installer = PluginInstaller(env=env, debug=False)
        with pytest.raises(OSError):
            installer.setup_plugins_dir()
