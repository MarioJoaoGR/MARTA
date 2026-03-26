
import pytest
from isort.parse import file_contents, Config, ParsedContent, DEFAULT_CONFIG

def test_valid_case():
    """Test standard input with valid Python code containing import statements."""
    contents = "import os\nfrom math import sqrt"
    config = Config()  # Using default configuration
    
    parsed_content = file_contents(contents, config=config)
    
    assert isinstance(parsed_content, ParsedContent)
    assert len(parsed_content.lines_without_imports) == 0
    assert "import os" in parsed_content.in_lines
    assert "from math import sqrt" in parsed_content.in_lines
