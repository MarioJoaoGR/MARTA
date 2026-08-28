
import pytest
from ansible.module_utils.splitter import _count_jinja2_blocks


def test_edge_case_none():
    with pytest.raises(ModuleNotFoundError):
        raise ModuleNotFoundError("Mocked error for testing purposes")
