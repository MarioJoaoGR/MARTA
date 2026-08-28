
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.pip import _have_pip_module


@patch('builtins.__import__', side_effect=ImportError)
def test_mocked_import_error(_):
    with pytest.raises(ImportError):
        _have_pip_module()