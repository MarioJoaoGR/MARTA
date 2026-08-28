
import pytest
from unittest.mock import patch
from ansible.module_utils.connection import Connection


def test_invalid_input():
    with pytest.raises(AssertionError) as excinfo:
        try:
            bad_conn = Connection(None)
        except AssertionError as e:
            raise e
    assert isinstance(excinfo.value, AssertionError)