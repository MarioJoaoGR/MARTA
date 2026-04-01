
import pytest
from pytutils.lazy.lazy_import import lazy_import

class ImportReplacer:
    pass

class ImportProcessor:
    """Convert text that users input into lazy import requests"""
    __slots__ = ['imports', '_lazy_import_class']
    
    def __init__(self, lazy_import_class=None):
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _canonicalize_import_text(self, text):
        """Take a list of imports, and split it into regularized form."""
        out = []
        cur = None
        continuing = False

        for line in text.split('\n'):
            line = line.strip()
            loc = line.find('#')
            if loc != -1:
                line = line[:loc].strip()

            if not line:
                continue
            if cur is not None:
                if line.endswith(')'):
                    out.append(cur + ' ' + line[:-1])
                    cur = None
                else:
                    cur += ' ' + line
            else:
                if '(' in line and ')' not in line:
                    cur = line.replace('(', '')
                else:
                    out.append(line.replace('(', '').replace(')', ''))
        if cur is not None:
            raise ValueError('Unmatched parenthesis')
        return out

def test_invalid_input():
    processor = ImportProcessor()
    
    # Test with invalid input that should raise a ValueError
    with pytest.raises(ValueError):
        processor._canonicalize_import_text("from bzrlib import foo, bar ( baz")
