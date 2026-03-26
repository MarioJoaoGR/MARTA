
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS

def test_invalid_input():
    parser = NumpydocParser()
    
    # Attempt to add a section with an invalid type (string instead of Section)
    with pytest.raises(TypeError):
        parser.add_section("Invalid Input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        parser = NumpydocParser()
    
        # Attempt to add a section with an invalid type (string instead of Section)
        with pytest.raises(TypeError):
>           parser.add_section("Invalid Input")

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/numpydoc.py:326: in add_section
    self._setup()
docstring_parser/docstring_parser/numpydoc.py:315: in _setup
    r"|".join(s.title_pattern for s in self.sections.values()),
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <dict_valueiterator object at 0x103b9ed90>

>       r"|".join(s.title_pattern for s in self.sections.values()),
        flags=re.M,
    )
E   AttributeError: 'str' object has no attribute 'title_pattern'

docstring_parser/docstring_parser/numpydoc.py:315: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""