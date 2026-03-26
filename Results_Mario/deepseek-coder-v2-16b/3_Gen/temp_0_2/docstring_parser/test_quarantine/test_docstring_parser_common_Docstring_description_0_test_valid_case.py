
import pytest
from docstring_parser.common import Docstring, DocstringStyle

def test_valid_case():
    # Creating a Docstring object without specifying style
    doc = Docstring()
    assert doc.style is None
    
    # Creating a Docstring object with a specified style
    custom_style = DocstringStyle("custom")
    doc_with_style = Docstring(style=custom_style)
    assert doc_with_style.style == "custom"

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

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_description_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Creating a Docstring object without specifying style
        doc = Docstring()
        assert doc.style is None
    
        # Creating a Docstring object with a specified style
>       custom_style = DocstringStyle("custom")

docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_description_0_test_valid_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/enum.py:385: in __call__
    return cls.__new__(cls, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <enum 'DocstringStyle'>, value = 'custom'

    def __new__(cls, value):
        # all enum instances are actually created during class construction
        # without calling this method; this method is called by the metaclass'
        # __call__ (i.e. Color(3) ), and by pickle
        if type(value) is cls:
            # For lookups like Color(Color.RED)
            return value
        # by-value search for a matching enum member
        # see if it's in the reverse mapping (for hashable values)
        try:
            return cls._value2member_map_[value]
        except KeyError:
            # Not found, no need to do long O(n) search
            pass
        except TypeError:
            # not there, now do long search -- O(n) behavior
            for member in cls._member_map_.values():
                if member._value_ == value:
                    return member
        # still not found -- try _missing_ hook
        try:
            exc = None
            result = cls._missing_(value)
        except Exception as e:
            exc = e
            result = None
        try:
            if isinstance(result, cls):
                return result
            else:
                ve_exc = ValueError("%r is not a valid %s" % (value, cls.__qualname__))
                if result is None and exc is None:
>                   raise ve_exc
E                   ValueError: 'custom' is not a valid DocstringStyle

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/enum.py:710: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_description_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.04s ===============================
"""