
from isort.core import _indented_config, Config
import pytest

@pytest.fixture
def sample_config():
    return Config(line_length=80, wrap_length=79)

def test_edge_case_empty_indent(sample_config):
    # Test when indent is an empty string
    result = _indented_config(sample_config, "")
    assert result == sample_config

    # Test when indent is a non-empty string
    indented_config = _indented_config(sample_config, "    ")  # Indent with four spaces
    assert isinstance(indented_config, Config)
    assert indented_config.line_length == max(sample_config.line_length - len("    "), 0)
    assert indented_config.wrap_length == max(sample_config.wrap_length - len("    "), 0)
