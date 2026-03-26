# Module: isort.deprecated.finders
# test_KnownPatternFinder.py
import re
from unittest.mock import MagicMock

from isort.deprecated.finders import KnownPatternFinder


def test_init():
    config = MagicMock()
    finder = KnownPatternFinder(config)
    assert hasattr(finder, 'known_patterns')
    assert isinstance(finder.known_patterns, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in finder.known_patterns)
    assert all(isinstance(pattern[0], re.Pattern) and isinstance(pattern[1], str) for pattern, _ in finder.known_patterns)

def test_find():
    config = MagicMock()
    finder = KnownPatternFinder(config)
    
    # Mock known patterns
    known_patterns = [
        (re.compile("^module$"), "section1"),
        (re.compile("^module\\..+$"), "section2")
    ]
    finder.known_patterns = known_patterns
    
    assert finder.find("module") == "section1"
    assert finder.find("module.submodule") == "section2"
    assert finder.find("othermodule") is None

def test_find_with_complex_module_name():
    config = MagicMock()
    finder = KnownPatternFinder(config)
    
    # Mock known patterns
    known_patterns = [
        (re.compile("^module$"), "section1"),
        (re.compile("^module\\..+$"), "section2")
    ]
    finder.known_patterns = known_patterns
    
    assert finder.find("module.submodule.deepmodule") == "section2"
    assert finder.find("module.submodule") == "section2"
    assert finder.find("module") == "section1"

def test_find_with_no_patterns():
    config = MagicMock()
    finder = KnownPatternFinder(config)
    
    # No known patterns
    finder.known_patterns = []
    
    assert finder.find("anymodule") is None
