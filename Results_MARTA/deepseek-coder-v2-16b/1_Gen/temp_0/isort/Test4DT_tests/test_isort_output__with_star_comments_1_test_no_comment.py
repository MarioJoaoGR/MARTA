
import pytest
from unittest.mock import MagicMock
from isort.output import _with_star_comments

def test_no_comment():
    parsed = MagicMock()
    parsed.categorized_comments = {'nested': {'module1': {}, 'module2': {}}}
    
    comments = ["Initial comment"]
    result = _with_star_comments(parsed, "module1", comments)
    assert result == ["Initial comment"]
    
    # Test with a module that has no "*"-type comments
    parsed.categorized_comments["nested"]["module3"] = {}
    result = _with_star_comments(parsed, "module3", comments)
    assert result == ["Initial comment"]
