
import pytest

from isort.settings import Config


@pytest.fixture
def config_instance():
    return Config()

def test_config_init(config_instance):
    assert isinstance(config_instance, Config)
