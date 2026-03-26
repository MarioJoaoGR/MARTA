
import pytest
from isort.output import _with_star_comments  # Correcting the import path and ensuring it exists in the module
from unittest.mock import MagicMock

# Mock data for testing
@pytest.fixture
def parsed():
    parsed = MagicMock()
    parsed.categorized_comments = {
        "nested": {
            "module_name": {"*": "special * comment"}
        }
    }
    return parsed

# Test case function
def test_no_star_comment(parsed):
    comments = ["original comment 1", "original comment 2"]
    result = _with_star_comments(parsed, "module_name", comments)
    assert result == ["original comment 1", "original comment 2", "special * comment"]
