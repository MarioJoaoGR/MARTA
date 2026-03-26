
import pytest

from isort.wrap_modes import vertical_prefix_from_module_import


def test_vertical_prefix_from_module_import_with_comments():
    interface = {
        "imports": ["from module1 import function1", "import function2"],
        "statement": "from prefix_module import",
        "comments": ["# Comment for the first import", "# Another comment for the second import"],
        "remove_comments": False,
        "comment_prefix": "#",
        "line_length": 50,
        "line_separator": "\n"
    }
    result = vertical_prefix_from_module_import(**interface)
    assert isinstance(result, str), "The result should be a string."
    lines = result.split("\n")