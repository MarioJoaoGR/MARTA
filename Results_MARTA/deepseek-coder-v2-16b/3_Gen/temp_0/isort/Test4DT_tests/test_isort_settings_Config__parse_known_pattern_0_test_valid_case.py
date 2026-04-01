
import pytest

from isort.settings import Config


@pytest.fixture
def config_instance():
    return Config(config=None)

def test_config_initialization(config_instance):
    assert isinstance(config_instance, Config)
    assert config_instance._known_patterns is None
    assert config_instance._section_comments is None
    assert config_instance._section_comments_end is None
    assert config_instance._skips is None
    assert config_instance._skip_globs is None
    assert config_instance._sorting_function is None
