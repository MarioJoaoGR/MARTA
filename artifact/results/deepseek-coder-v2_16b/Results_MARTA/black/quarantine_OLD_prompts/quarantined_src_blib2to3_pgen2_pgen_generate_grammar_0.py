
import pytest
from unittest.mock import patch
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar

def generate_grammar(filename: Path = "Grammar.txt") -> PgenGrammar:
    p = ParserGenerator(filename)
    return p.make_grammar()

@pytest.mark.parametrize("filename", [None, "custom_grammar.txt"])
def test_default_filename(mock_parser, filename):
    with patch('blib2to3.pgen2.pgen.ParserGenerator', autospec=True) as mock_parser:
        mock_instance = mock_parser.return_value
        mock_instance.make_grammar.return_value = PgenGrammar()

        if filename is None:
            grammar = generate_grammar()
        else:
            grammar = generate_grammar(filename)

        assert isinstance(grammar, PgenGrammar), "Generated grammar should be an instance of PgenGrammar"
        mock_parser.assert_called_once_with("Grammar.txt") if filename is None else mock_parser.assert_called_once_with(filename)

def test_custom_filename():
    with patch('blib2to3.pgen2.pgen.ParserGenerator', autospec=True) as mock_parser:
        mock_instance = mock_parser.return_value
        mock_instance.make_grammar.return_value = PgenGrammar()

        grammar = generate_grammar("custom_grammar.txt")

        assert isinstance(grammar, PgenGrammar), "Generated grammar should be an instance of PgenGrammar"
        mock_parser.assert_called_once_with("custom_grammar.txt")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_src_blib2to3_pgen2_pgen_generate_grammar_0.py ______
/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_pgen_generate_grammar_0.py:6: in <module>
    def generate_grammar(filename: Path = "Grammar.txt") -> PgenGrammar:
E   NameError: name 'Path' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_pgen_generate_grammar_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""