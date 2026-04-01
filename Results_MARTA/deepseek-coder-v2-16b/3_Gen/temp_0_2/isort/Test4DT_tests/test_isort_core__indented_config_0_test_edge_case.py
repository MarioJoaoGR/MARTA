
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

# Test case for _indented_config function
def test_indented_config():
    # Create a mock Config object
    existing_config = Config()
    
    # Define the indent string
    indent = "    "  # Four spaces
    
    # Call the function with the mock config and indent
    modified_config = _indented_config(existing_config, indent)
    
    # Assert that the line length and wrap length have been adjusted correctly
    assert modified_config.line_length == max(existing_config.line_length - len(indent), 0)
    assert modified_config.wrap_length == max(existing_config.wrap_length - len(indent), 0)
    
    # Optionally, you can add more assertions to ensure other properties are correctly set
