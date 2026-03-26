
import pytest
from isort.core import Config

def _indented_config(config: Config, indent: str) -> Config:
    if not indent:
        return config

    return Config(
        config=config,
        line_length=max(config.line_length - len(indent), 0),
        wrap_length=max(config.wrap_length - len(indent), 0),
        lines_after_imports=1,
        import_headings=config.import_headings if config.indented_import_headings else {},
        import_footers=config.import_footers if config.indented_import_headings else {},
    )

# Test case for valid input
def test_valid_input():
    initial_config = Config()
    
    # No indentation (should return the original config)
    no_indentation_config = _indented_config(initial_config, "")
    assert no_indentation_config == initial_config
    
    # With indentation
    indented_config = _indented_config(initial_config, "    ")  # Applying 4 spaces of indentation
    assert indented_config.line_length == max(initial_config.line_length - 4, 0)
    assert indented_config.wrap_length == max(initial_config.wrap_length - 4, 0)
    assert indented_config.lines_after_imports == 1
    
    # Ensure other config properties remain unchanged unless explicitly overridden
    assert indented_config.import_headings == initial_config.import_headings
    assert indented_config.import_footers == initial_config.import_footers
