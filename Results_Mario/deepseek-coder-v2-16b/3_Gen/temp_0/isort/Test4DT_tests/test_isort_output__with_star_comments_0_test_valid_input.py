
import pytest
from unittest.mock import MagicMock
from isort.output import _with_star_comments

def test_valid_input():
    parsed = MagicMock()
    parsed.categorized_comments = {"nested": {"module1": {"*": "This is a * comment for module1"}, "module2": {}}}
    
    result = _with_star_comments(parsed, "module1", ["Initial comment"])
    assert result == ['Initial comment', 'This is a * comment for module1']
    
    # Test case where the module does not have a "*"-type comment
    parsed.categorized_comments["nested"]["module1"].pop("*", None)  # Use pop with default value to avoid KeyError
