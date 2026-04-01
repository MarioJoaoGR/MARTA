
from isort.core import Config, _indented_config

def test_valid_inputs():
    # Create an instance of Config for testing
    config = Config()
    
    # Test with a valid indent string
    indented_config = _indented_config(config, "    ")  # Indents with four spaces
    assert isinstance(indented_config, Config)
    assert indented_config.line_length == max(config.line_length - len("    "), 0)
    assert indented_config.wrap_length == max(config.wrap_length - len("    "), 0)
    
    # Test with an empty string (should return the original config without changes)
    no_change_config = _indented_config(config, "")
    assert no_change_config is config
