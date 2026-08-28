
import pytest
from apimd.loader import loader

# Test with default values
def test_loader_default():
    result = loader('/path/to/root', '/path/to/working_dir', True, 2, True)
    assert isinstance(result, str), "Expected a string representation of the documentation."

# Test without links and TOC enabled
def test_loader_no_links_toc():
    result = loader('/path/to/root', '/path/to/working_dir', False, 2, False)
    assert isinstance(result, str), "Expected a string representation of the documentation."

# Test with detailed level set to 1 (not detailed)
def test_loader_low_detail_level():
    result = loader('/path/to/root', '/path/to/working_dir', True, 1, True)
    assert isinstance(result, str), "Expected a string representation of the documentation."

# Test with working directory different from root
def test_loader_different_pwd():
    result = loader('/path/to/root', '/different/working/directory', True, 2, True)
    assert isinstance(result, str), "Expected a string representation of the documentation."

# Test with all parameters set to default except for link being False
def test_loader_default_except_link():
    result = loader('/path/to/root', '/path/to/working_dir', False, 2, True)
    assert isinstance(result, str), "Expected a string representation of the documentation."
