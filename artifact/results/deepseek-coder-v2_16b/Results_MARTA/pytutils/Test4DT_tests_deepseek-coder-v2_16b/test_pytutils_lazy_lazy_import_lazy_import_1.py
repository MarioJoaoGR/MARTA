
import pytest
from pytutils.lazy.lazy_import import lazy_import, ImportProcessor


def test_lazy_import_custom_class():
    with pytest.raises(ModuleNotFoundError):
        from my_custom_module import MyCustomLazyImport
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
        proc = ImportProcessor()
        lazy_import(scope, text)
