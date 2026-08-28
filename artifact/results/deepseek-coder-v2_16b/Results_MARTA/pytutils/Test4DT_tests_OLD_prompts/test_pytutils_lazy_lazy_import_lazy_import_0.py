
import pytest
from pytutils.lazy.lazy_import import lazy_import
from unittest.mock import patch, MagicMock

def test_lazy_import_basic():
    with patch('pytutils.lazy.lazy_import.ImportProcessor') as mock_proc:
        scope = globals()
        text = """
        from bzrlib import (
            foo,
            bar,
            baz,
        )
        import bzrlib.branch
        import bzrlib.transport
        """
        lazy_import(scope, text)
        mock_proc.assert_called_once_with(lazy_import_class=None)
        mock_proc().lazy_import.assert_called_once_with(scope, text)


def test_lazy_import_multiline_string():
    with patch('pytutils.lazy.lazy_import.ImportProcessor') as mock_proc:
        scope = globals()
        text = """
        from bzrlib import (
            foo,
            bar,
            baz,
        )
        import bzrlib.branch
        import bzrlib.transport
        """
        lazy_import(scope, text)
        mock_proc.assert_called_once_with(lazy_import_class=None)
        mock_proc().lazy_import.assert_called_once_with(scope, text)