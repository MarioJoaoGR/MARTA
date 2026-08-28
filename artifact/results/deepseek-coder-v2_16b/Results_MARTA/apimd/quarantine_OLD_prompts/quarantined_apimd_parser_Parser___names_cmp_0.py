
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
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___names_cmp_0.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        p = Parser()
        with pytest.raises(TypeError):
>           p.parse(123, "test content")

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___names_cmp_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={123: '## Module `{}`\n<a id="{}"></a>\n\n'}, docstring={}, imp={}, root={}, alias={}, const={})
root = 123, script = 'test content'

    def parse(self, root: str, script: str) -> None:
        """Main parser of the entire module."""
        self.doc[root] = '#' * self.b_level + "# Module `{}`"
        if self.link:
            self.doc[root] += "\n<a id=\"{}\"></a>"
        self.doc[root] += '\n\n'
>       self.level[root] = root.count('.')
E       AttributeError: 'int' object has no attribute 'count'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:309: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_Parser___names_cmp_0.py::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""