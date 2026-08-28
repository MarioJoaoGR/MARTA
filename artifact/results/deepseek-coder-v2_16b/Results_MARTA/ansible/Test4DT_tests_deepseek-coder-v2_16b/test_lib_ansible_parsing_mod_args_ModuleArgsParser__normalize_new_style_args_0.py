
import pytest
from ansible.parsing.mod_args import ModuleArgsParser
from ansible.errors import AnsibleAssertionError, AnsibleParserError


def test_edge_cases():
    task_ds = None
    with pytest.raises(AnsibleParserError):
        parser = ModuleArgsParser(task_ds=task_ds)
        action, args, delegate_to = parser.parse()
