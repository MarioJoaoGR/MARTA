
import pytest
from ansible.plugins.filter.core import quote


def test_quote_without_spaces():
    assert quote('no_spaces') == 'no_spaces'

