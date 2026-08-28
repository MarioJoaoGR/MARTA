
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

# Assuming DEFAULT_SECTIONS is defined in the module and contains 'Parameters' and 'Returns'
DEFAULT_SECTIONS = {
    'Parameters': Section(title="Parameters"),
    'Returns': Section(title="Returns")
}

def test_numpydocparser_with_default_sections():
    parser = NumpydocParser()
    assert len(parser.sections) == 2
    assert set(parser.sections.keys()) == {'Parameters', 'Returns'}

def test_numpydocparser_with_custom_sections():
    custom_section1 = Section(title="Custom Section 1", key="custom1")
    custom_section2 = Section(title="Custom Section 2", key="custom2")
    custom_sections = {
        'Custom Section 1': custom_section1,
        'Custom Section 2': custom_section2
    }
    parser = NumpydocParser(sections=custom_sections)
    assert len(parser.sections) == 2
    assert set(parser.sections.keys()) == {'Custom Section 1', 'Custom Section 2'}

def test_numpydocparser_with_empty_custom_sections():
    empty_sections = {}
    parser = NumpydocParser(sections=empty_sections)
    assert len(parser.sections) == 2
    assert set(parser.sections.keys()) == {'Parameters', 'Returns'}

def test_numpydocparser_with_none_custom_sections():
    parser = NumpydocParser(sections=None)
    assert len(parser.sections) == 2
    assert set(parser.sections.keys()) == {'Parameters', 'Returns'}

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
_ ERROR collecting test_docstring_parser_numpydoc_NumpydocParser___init___0.py _
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_NumpydocParser___init___0.py:7: in <module>
    'Parameters': Section(title="Parameters"),
E   TypeError: Section.__init__() missing 1 required positional argument: 'key'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_numpydoc_NumpydocParser___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""