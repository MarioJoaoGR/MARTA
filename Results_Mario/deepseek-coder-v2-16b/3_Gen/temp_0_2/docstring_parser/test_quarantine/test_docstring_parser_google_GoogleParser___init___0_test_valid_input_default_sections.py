
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_valid_input_default_sections():
    parser = GoogleParser()
    assert isinstance(parser, GoogleParser)
    assert parser.title_colon is True
    assert len(parser.sections) == 0

def test_valid_input_custom_sections():
    from docstring_parser.google import Section
    custom_sections = [Section('Summary'), Section('Parameters')]
    parser = GoogleParser(custom_sections, title_colon=False)
    assert len(parser.sections) == 2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser___init___0_test_valid_input_default_sections.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_default_sections _______________________

    def test_valid_input_default_sections():
        parser = GoogleParser()
        assert isinstance(parser, GoogleParser)
        assert parser.title_colon is True
>       assert len(parser.sections) == 0
E       AssertionError: assert 12 == 0
E        +  where 12 = len({'Args': Section(title='Args', key='param', type=<SectionType.MULTIPLE: 1>), 'Arguments': Section(title='Arguments', k...e=<SectionType.MULTIPLE: 1>), 'Example': Section(title='Example', key='examples', type=<SectionType.SINGULAR: 0>), ...})
E        +    where {'Args': Section(title='Args', key='param', type=<SectionType.MULTIPLE: 1>), 'Arguments': Section(title='Arguments', k...e=<SectionType.MULTIPLE: 1>), 'Example': Section(title='Example', key='examples', type=<SectionType.SINGULAR: 0>), ...} = <docstring_parser.google.GoogleParser object at 0x1066cfee0>.sections

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser___init___0_test_valid_input_default_sections.py:9: AssertionError
_______________________ test_valid_input_custom_sections _______________________

    def test_valid_input_custom_sections():
        from docstring_parser.google import Section
>       custom_sections = [Section('Summary'), Section('Parameters')]
E       TypeError: SectionBase.__new__() missing 2 required positional arguments: 'key' and 'type'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser___init___0_test_valid_input_default_sections.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser___init___0_test_valid_input_default_sections.py::test_valid_input_default_sections
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser___init___0_test_valid_input_default_sections.py::test_valid_input_custom_sections
============================== 2 failed in 0.03s ===============================
"""