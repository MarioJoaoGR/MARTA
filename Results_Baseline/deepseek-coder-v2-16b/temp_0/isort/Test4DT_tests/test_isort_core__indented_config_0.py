
# Module: isort.core
# test_isort_core.py
from isort.core import Config, _indented_config


def test_indented_config_with_valid_indent():
    # Arrange
    mock_config = Config(line_length=80, wrap_length=79)
    
    # Act
    result = _indented_config(mock_config, "    ")
    
    # Assert
    assert result.line_length == 76
    assert result.wrap_length == 75

def test_indented_config_with_empty_indent():
    # Arrange
    mock_config = Config(line_length=80, wrap_length=79)
    
    # Act
    result = _indented_config(mock_config, "")
    
    # Assert
    assert result.line_length == 80