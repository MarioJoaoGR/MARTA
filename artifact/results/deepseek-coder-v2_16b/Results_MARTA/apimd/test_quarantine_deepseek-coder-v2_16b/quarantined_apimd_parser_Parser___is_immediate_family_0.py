
import pytest
from apimd.parser import Parser



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        p = Parser()
        p.root['example'] = 'ex'
        n1 = 'example'
        n2 = 'examples'
>       assert p._Parser__is_immediate_family(n1, n2) is True

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={'example': 'ex'}, alias={}, const={})
n1 = 'example', n2 = 'examples'

    def __is_immediate_family(self, n1: str, n2: str) -> bool:
        """Check the name is immediate family."""
>       return n2.startswith(n1.removesuffix(n2.removeprefix(self.root[n2])))
E       KeyError: 'examples'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:530: KeyError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        p = Parser()
        p.root[''] = ''
        n1 = None
        n2 = ''
        with pytest.raises(TypeError):  # Ensure TypeError for invalid input types
>           assert p._Parser__is_immediate_family(n1, n2) is False

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={'': ''}, alias={}, const={})
n1 = None, n2 = ''

    def __is_immediate_family(self, n1: str, n2: str) -> bool:
        """Check the name is immediate family."""
>       return n2.startswith(n1.removesuffix(n2.removeprefix(self.root[n2])))
E       AttributeError: 'NoneType' object has no attribute 'removesuffix'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:530: AttributeError
_______________________________ test_error_case ________________________________

    def test_error_case():
        p = Parser()
        p.root['invalid'] = 'inv'
        n1 = 'invalid'
        n2 = 'valid'
        with pytest.raises(AssertionError):  # Ensure assertion error for invalid comparison
>           assert p._Parser__is_immediate_family(n1, n2) is False

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={'invalid': 'inv'}, alias={}, const={})
n1 = 'invalid', n2 = 'valid'

    def __is_immediate_family(self, n1: str, n2: str) -> bool:
        """Check the name is immediate family."""
>       return n2.startswith(n1.removesuffix(n2.removeprefix(self.root[n2])))
E       KeyError: 'valid'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:530: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___is_immediate_family_0.py::test_error_case
============================== 3 failed in 0.09s ===============================
"""