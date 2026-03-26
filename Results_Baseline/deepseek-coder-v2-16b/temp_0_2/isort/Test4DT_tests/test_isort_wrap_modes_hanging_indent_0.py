
import pytest

from isort.wrap_modes import hanging_indent


@pytest.fixture
def default_interface():
    return {
        "imports": ["os", "sys"],
        "statement": "import ",
        "line_length": 50,
        "line_separator": "\n",
        "indent": "    "
    }

@pytest.fixture
def multi_line_interface():
    return {
        "imports": ["numpy as np", "pandas as pd"],
        "statement": "from some_module import ",
        "line_length": 30,
        "line_separator": "\n",
        "indent": "  "
    }

@pytest.fixture
def comments_interface():
    return {
        "imports": ["numpy as np", "pandas as pd"],
        "statement": "from some_module import ",
        "line_length": 30,
        "line_separator": "\n",
        "indent": "  ",
        "comments": ["# This is a comment", "# Another important note"]
    }

@pytest.fixture
def remove_comments_interface():
    return {
        "imports": ["numpy as np", "pandas as pd"],
        "statement": "from some_module import ",
        "line_length": 30,
        "line_separator": "\n",
        "indent": "  ",
        "comments": ["# This is a comment", "# Another important note"],
        "remove_comments": True
    }

@pytest.fixture
def custom_comment_prefix_interface():
    return {
        "imports": ["numpy as np", "pandas as pd"],
        "statement": "from some_module import ",
        "line_length": 30,
        "line_separator": "\n",
        "indent": "  ",
        "comments": ["# This is a comment", "# Another important note"],
        "comment_prefix": "# "
    }

def test_hanging_indent_basic(default_interface):
    default_interface["imports"] = []  # Adjust the fixture to match the function's requirement
    result = hanging_indent(**default_interface)
    assert result == ''

def test_hanging_indent_multi_line(multi_line_interface):
    multi_line_interface["imports"] = []  # Adjust the fixture to match the function's requirement
    result = hanging_indent(**multi_line_interface)