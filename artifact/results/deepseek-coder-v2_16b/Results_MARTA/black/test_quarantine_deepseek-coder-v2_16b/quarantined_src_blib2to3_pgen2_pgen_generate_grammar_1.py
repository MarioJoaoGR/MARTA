
import pytest
from pathlib import Path
from blib2to3.pgen2.pgen_generate import generate_grammar, PgenGrammar
from unittest.mock import patch

# Test case to check if the default filename "Grammar.txt" is used when no argument is provided
def test_default_filename():
    with patch('blib2to3.pgen2.pgen_generate.ParserGenerator') as mock_parser:
        # Mocking the ParserGenerator instantiation and make_grammar method
        mock_parser.return_value.make_grammar.return_value = PgenGrammar()
        
        grammar = generate_grammar()
        
        assert isinstance(grammar, PgenGrammar)
        mock_parser.assert_called_with("Grammar.txt")

# Test case to check if a custom filename is used when provided as an argument
def test_custom_filename():
    custom_filename = "custom_grammar.txt"
    with patch('blib2to3.pgen2.pgen_generate.ParserGenerator') as mock_parser:
        # Mocking the ParserGenerator instantiation and make_grammar method
        mock_parser.return_value.make_grammar.return_value = PgenGrammar()
        
        grammar = generate_grammar(custom_filename)
        
        assert isinstance(grammar, PgenGrammar)
        mock_parser.assert_called_with(custom_filename)

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
_____ ERROR collecting test_src_blib2to3_pgen2_pgen_generate_grammar_1.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_pgen_generate_grammar_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_pgen_generate_grammar_1.py:4: in <module>
    from blib2to3.pgen2.pgen_generate import generate_grammar, PgenGrammar
E   ModuleNotFoundError: No module named 'blib2to3.pgen2.pgen_generate'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_pgen_generate_grammar_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""