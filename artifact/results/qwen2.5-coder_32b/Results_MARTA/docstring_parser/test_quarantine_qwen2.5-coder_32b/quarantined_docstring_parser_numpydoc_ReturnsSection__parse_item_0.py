
import pytest
from docstring_parser.numpydoc import NumpydocReturnsParser, DocstringReturns

def _clean_str(s):
    return s.strip()

# Test parsing a return section with both name and type
def test_parse_item_with_name_and_type():
    parser = NumpydocReturnsParser()
    result = parser._parse_item("result: int", "The sum of two numbers")
    assert isinstance(result, DocstringReturns)
    assert result.description == "The sum of two numbers"
    assert result.type_name == "int"
    assert result.return_name == "result"

# Test parsing a return section with only type
def test_parse_item_with_only_type():
    parser = NumpydocReturnsParser()
    result = parser._parse_item("str", "Yields the next string in sequence")
    assert isinstance(result, DocstringReturns)
    assert result.description == "Yields the next string in sequence"
    assert result.type_name is None
    assert result.return_name is None

# Test parsing a generator's yield section with name and type
def test_parse_item_generator_with_name_and_type():
    parser = NumpydocReturnsParser(is_generator=True)
    result = parser._parse_item("next_string: str", "Yields the next string in sequence")
    assert isinstance(result, DocstringReturns)
    assert result.description == "Yields the next string in sequence"
    assert result.type_name == "str"
    assert result.return_name == "next_string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_docstring_parser_numpydoc_ReturnsSection__parse_item_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0.py:3: in <module>
    from docstring_parser.numpydoc import NumpydocReturnsParser, DocstringReturns
E   ImportError: cannot import name 'NumpydocReturnsParser' from 'docstring_parser.numpydoc' (/opt/marta/baselines/codamosa/replication/test-apps/docstring_parser/docstring_parser/numpydoc.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_ReturnsSection__parse_item_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""