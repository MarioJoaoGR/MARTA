
import pytest

from isort import settings
from isort.settings import _Config


def test_valid_case():
    # Arrange
    config = _Config(py_version='3', line_length=80)
    
    # Act and Assert
    assert config.line_length == 80
    assert config.py_version == 'py3'
    assert isinstance(config.skip, frozenset)
    assert config.wrap_length <= config.line_length
    assert not hasattr(config, "unknown_attribute")  # Ensure no unknown attributes are present

if __name__ == "__main__":
    pytest.main()
