
import pytest
from apimd.parser import Parser





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________________ test_Parser_is_public_os_path_join ______________________

    def test_Parser_is_public_os_path_join():
        p = Parser()
>       assert p.is_public('os.path.join') is True

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
s = 'os.path.join'

    def is_public(self, s: str) -> bool:
        """Check the name is public style or listed in `__all__`."""
        if s in self.imp:
            for ch in chain(self.doc.keys(), self.const.keys()):
                if ch.startswith(s + '.') and is_public_family(ch):
                    break
            else:
                return False
>       all_l = self.imp[self.root[s]]
E       KeyError: 'os.path.join'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:558: KeyError
________________ test_Parser_is_public_private_module_function _________________

    def test_Parser_is_public_private_module_function():
        p = Parser()
>       assert p.is_public('_private_module.function') is False

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
s = '_private_module.function'

    def is_public(self, s: str) -> bool:
        """Check the name is public style or listed in `__all__`."""
        if s in self.imp:
            for ch in chain(self.doc.keys(), self.const.keys()):
                if ch.startswith(s + '.') and is_public_family(ch):
                    break
            else:
                return False
>       all_l = self.imp[self.root[s]]
E       KeyError: '_private_module.function'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:558: KeyError
______________________ test_Parser_is_public_magic_method ______________________

    def test_Parser_is_public_magic_method():
        p = Parser()
>       assert p.is_public('__magic__.method') is False

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
s = '__magic__.method'

    def is_public(self, s: str) -> bool:
        """Check the name is public style or listed in `__all__`."""
        if s in self.imp:
            for ch in chain(self.doc.keys(), self.const.keys()):
                if ch.startswith(s + '.') and is_public_family(ch):
                    break
            else:
                return False
>       all_l = self.imp[self.root[s]]
E       KeyError: '__magic__.method'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:558: KeyError
______________________ test_Parser_is_public_module_init _______________________

    def test_Parser_is_public_module_init():
        p = Parser()
>       assert p.is_public('module.__init__') is False

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
s = 'module.__init__'

    def is_public(self, s: str) -> bool:
        """Check the name is public style or listed in `__all__`."""
        if s in self.imp:
            for ch in chain(self.doc.keys(), self.const.keys()):
                if ch.startswith(s + '.') and is_public_family(ch):
                    break
            else:
                return False
>       all_l = self.imp[self.root[s]]
E       KeyError: 'module.__init__'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:558: KeyError
___________________ test_Parser_is_public_public_module_name ___________________

    def test_Parser_is_public_public_module_name():
        p = Parser()
>       assert p.is_public('public.module.name') is True

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
s = 'public.module.name'

    def is_public(self, s: str) -> bool:
        """Check the name is public style or listed in `__all__`."""
        if s in self.imp:
            for ch in chain(self.doc.keys(), self.const.keys()):
                if ch.startswith(s + '.') and is_public_family(ch):
                    break
            else:
                return False
>       all_l = self.imp[self.root[s]]
E       KeyError: 'public.module.name'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:558: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py::test_Parser_is_public_os_path_join
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py::test_Parser_is_public_private_module_function
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py::test_Parser_is_public_magic_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py::test_Parser_is_public_module_init
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_is_public_0.py::test_Parser_is_public_public_module_name
============================== 5 failed in 0.13s ===============================
"""