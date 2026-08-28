
import pytest
import os
import tempfile
from ansible.modules.lineinfile import write_changes
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def module():
    # Create a mock Ansible module object
    module = MagicMock()
    module.params = {'validate': None}  # Default validate parameter
    module.tmpdir = tempfile.gettempdir()
    return module

@pytest.fixture(scope="module")
def b_lines():
    return [b"line1\n"]

@pytest.fixture(scope="module")
def dest():
    return "path/to/destination"


def test_write_changes_with_invalid_validate(module, b_lines, dest):
    module.params = {'validate': 'python -c "import os; assert os.path.exists(\"%s\"), \\\"File does not exist.\\\""'}
    with pytest.raises(ValueError) as e:
        write_changes(module, b_lines, dest)
        assert str(e.value) == 'validate must contain %s: python -c "import os; assert os.path.exists(\"%s\"), \\\"File does not exist.\\\""' % (dest)
