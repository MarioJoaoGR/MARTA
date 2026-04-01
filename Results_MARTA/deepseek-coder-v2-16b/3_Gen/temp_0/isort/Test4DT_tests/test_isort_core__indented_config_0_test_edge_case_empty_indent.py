
import pytest

from isort.core import Config, _indented_config


@pytest.fixture
def sample_config():
    return Config(line_length=80, wrap_length=79)

def test_indented_config_with_empty_indent(sample_config):
    # Arrange
    indent = ""
    
    # Act
    result = _indented_config(sample_config, indent)
    
    # Assert
    assert result.line_length == 80
    assert result.wrap_length == 79

def test_indented_config_with_non_empty_indent(sample_config):
    # Arrange
    indent = "    "  # Four spaces
    
    # Act
    result = _indented_config(sample_config, indent)
    
    # Assert
    assert result.line_length == 76  # 80 - 4
    assert result.wrap_length == 75  # 79 - 4
