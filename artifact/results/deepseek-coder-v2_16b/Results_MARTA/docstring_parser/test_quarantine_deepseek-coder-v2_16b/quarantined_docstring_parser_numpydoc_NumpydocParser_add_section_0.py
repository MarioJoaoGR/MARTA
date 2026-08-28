
import pytest
from numpydoc import Section, DEFAULT_SECTIONS
from docstring_parser.numpydoc import NumpydocParser

def test_default_initialization():
    parser = NumpydocParser()
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == 2  # Default sections: Parameters and Returns

def test_custom_initialization():
    custom_sections = {
        'Parameters': Section('Parameters', r'^\s*Parameters\b'),
        'Returns': Section('Returns', r'^\s*Returns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == 2  # Custom sections: Parameters and Returns

def test_add_section():
    parser = NumpydocParser()
    new_section = Section('Example', r'^\s*Example\b')
    parser.add_section(new_section)
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == 3  # Default sections + Example
    assert 'Example' in parser.sections

def test_parse_docstring():
    custom_sections = {
        'Parameters': Section('Parameters', r'^\s*Parameters\b'),
        'Returns': Section('Returns', r'^\s*Returns\b')
    }
    parser = NumpydocParser(sections=custom_sections)
    docstring_text = """
    Some short description.

    Parameters:
        param1 (type): Description of param1.
        param2 (type): Description of param2.

    Returns:
        return_type: Description of the return value.
    """
    parsed_docstring = parser.parse(docstring_text)
    assert isinstance(parsed_docstring, dict)
    assert 'Parameters' in parsed_docstring
    assert 'Returns' in parsed_docstring

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_docstring_parser_numpydoc_NumpydocParser_add_section_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc_NumpydocParser_add_section_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc_NumpydocParser_add_section_0.py:3: in <module>
    from numpydoc import Section, DEFAULT_SECTIONS
E   ModuleNotFoundError: No module named 'numpydoc'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_deepseek-coder-v2_16b/test_docstring_parser_numpydoc_NumpydocParser_add_section_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""