
from pytutils.lazy import lazy_import
from pytutils.errors import InvalidImportLine

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
        """Take a list of imports, and split it into regularized form.

        This is meant to take regular import text, and convert it to
        the forms that the rest of the converters prefer.
        
        Args:
            text (str): A multi-line string containing Python import statements.
            
        Returns:
            list: A list of normalized import strings without comments or unnecessary whitespace.
        """
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
            raise InvalidImportLine(cur, 'Unmatched parenthesis')
        return out

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_1_test_edge_case_none
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_1_test_edge_case_none.py:3:0: E0401: Unable to import 'pytutils.errors' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_1_test_edge_case_none.py:3:0: E0611: No name 'errors' in module 'pytutils' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_1_test_edge_case_none.py:12:38: E0602: Undefined variable 'ImportReplacer' (undefined-variable)


"""