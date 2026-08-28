
import pytest
from ansible.module_utils.splitter import _count_jinja2_blocks


def test_count_jinja2_blocks_more_open():
    assert _count_jinja2_blocks("{{ block1 }} {{ block2 }} {{", 0, "{{", "}}") == 1

def test_count_jinja2_blocks_more_close():
    assert _count_jinja2_blocks("{{ block1 }} {{ block2 }} }}", 0, "{{", "}}") == 0