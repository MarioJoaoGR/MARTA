
from pathlib import Path
from io import StringIO
from typing import Iterator, Any
import pytest
from isort.api import find_imports_in_code, Config, DEFAULT_CONFIG, ImportKey

# Assuming `example.py` content for testing
example_code = """
def main():
    print("Hello, world!")
"""

@pytest.fixture
def config():
    return Config()

def test_find_imports_in_code(config):
    imports = list(find_imports_in_code(example_code, config=config))
    assert len(imports) == 0, "Expected no imports in the example code"
