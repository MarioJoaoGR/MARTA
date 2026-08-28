
import pytest
from youtube_dl.downloader.f4m import _add_ns

def test_edge_cases():
    with pytest.raises(TypeError):
        # Test that calling _add_ns without a property raises TypeError
        _add_ns()

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test that calling _add_ns with a non-integer version raises TypeError
        _add_ns('title', 'invalid_version')

def test_valid_property():
    assert _add_ns('title') == '{http://ns.adobe.com/f4m/1.0}title'

def test_specific_version():
    assert _add_ns('description', 2) == '{http://ns.adobe.com/f4m/2.0}description'
