
import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError

def test_post_process_args_no_options():
    with pytest.raises(ValueError) as excinfo:
        cli = InventoryCLI({})
    assert str(excinfo.value) == 'A non-empty list for args is required'

