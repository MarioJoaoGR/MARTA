
# Module: apimd.loader
import pytest
from apimd.loader import loader

def test_loader_basic():
    # Test with basic parameters
    output = loader('/path/to/packages', 'mypackage', link=True, level=2, toc=True)
    assert isinstance(output, str)

def test_loader_no_links():
    # Test without links
    output = loader('/another/path/to/packages', 'otherpackage', link=False, level=3, toc=False)
    assert isinstance(output, str)

def test_loader_minimal_params():
    # Test with minimal parameters (default values for link, level, and toc)
    output = loader('/yet/another/path/to/packages', 'minimalpackage', link=True, level=2, toc=True)
    assert isinstance(output, str)

def test_loader_high_level_parsing():
    # Test with a higher parsing level
    output = loader('/deep/path/to/packages', 'deeppackage', link=True, level=5, toc=True)
    assert isinstance(output, str)

def test_loader_nonexistent_root():
    # Test with a non-existent root directory
    try:
        loader('/nonexistent/path', 'mypackage', link=True, level=2, toc=True)
    except FileNotFoundError as e:
        pytest.fail(f"Unexpected FileNotFoundError: {e}")

def test_loader_empty_package_name():
    # Test with an empty package name
    try:
        loader('/path/to/packages', '', link=True, level=2, toc=True)
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError: {e}")

def test_loader_negative_level():
    # Test with a negative parsing level (edge case)
    output = loader('/path/to/packages', 'mypackage', link=True, level=-1, toc=True)
    assert isinstance(output, str)

def test_loader_zero_level():
    # Test with zero parsing level (edge case)
    output = loader('/path/to/packages', 'mypackage', link=True, level=0, toc=True)
    assert isinstance(output, str)

def test_loader_large_level():
    # Test with a very large parsing level
    output = loader('/path/to/packages', 'mypackage', link=True, level=100, toc=True)
    assert isinstance(output, str)
