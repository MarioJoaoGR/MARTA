
import pytest
from docstring_parser.google import GoogleParser, Section, DocstringParam, DocstringReturns, DocstringRaises

# Define default sections as per the error message and class initialization
DEFAULT_SECTIONS = [
    Section(title="Parameters", key="param"),
    Section(title="Returns", key="returns"),
    Section(title="Yields", key="yields"),
    Section(title="Raises", key="raises")
]

@pytest.fixture
def parser():
    return GoogleParser(sections=DEFAULT_SECTIONS)

def test_build_multi_meta_parameters(parser):
    section = Section(title="Parameters", key="param")
    before = "item_count: int, optional"
    desc = "The number of items to process."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringParam)
    assert meta.arg_name == "item_count"
    assert meta.type_name == "int"
    assert meta.is_optional is True
    assert meta.description == "The number of items to process."

def test_build_multi_meta_returns(parser):
    section = Section(title="Returns", key="returns")
    before = "int"
    desc = "The sum of two numbers."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringReturns)
    assert meta.type_name == "int"
    assert meta.description == "The sum of two numbers."

def test_build_multi_meta_yields(parser):
    section = Section(title="Yields", key="yields")
    before = "str"
    desc = "A string value."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringReturns)
    assert meta.type_name == "str"
    assert meta.description == "A string value."
    assert meta.is_generator is True

def test_build_multi_meta_raises(parser):
    section = Section(title="Raises", key="raises")
    before = "ValueError"
    desc = "If the input is out of range."
    
    meta = parser._build_multi_meta(section, before, desc)
    
    assert isinstance(meta, DocstringRaises)
    assert meta.type_name == "ValueError"
    assert meta.description == "If the input is out of range."

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
_ ERROR collecting test_docstring_parser_google_GoogleParser__build_multi_meta_0.py _
/opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py:7: in <module>
    Section(title="Parameters", key="param"),
E   TypeError: SectionBase.__new__() missing 1 required positional argument: 'type'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/docstring_parser/Test4DT_tests_qwen2.5-coder_32b/test_docstring_parser_google_GoogleParser__build_multi_meta_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""