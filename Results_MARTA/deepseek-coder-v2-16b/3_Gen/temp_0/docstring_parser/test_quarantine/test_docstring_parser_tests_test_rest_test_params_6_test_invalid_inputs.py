
from docstring_parser.tests.test_rest import parse

def test_invalid_inputs() -> None:
    """Test invalid inputs to check error handling."""
    # Test with an empty docstring
    docstring = parse("")
    assert len(docstring.params) == 0

    # Test with a malformed docstring (missing colon after parameter name)
    docstring = parse(
        """
        Short description

        :param name description 1
        :param int priority: description 2
        :param str? sender: description 3
        :param str? message: description 4, defaults to 'hello'
        :param str? multiline: long description 5,
        defaults to 'bye'
        """
    )
    assert len(docstring.params) == 0  # Expecting no parameters due to malformed input

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_6_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

text = "Short description\n\n:param name description 1\n:param int priority: description 2\n:param str? sender: description 3\n:param str? message: description 4, defaults to 'hello'\n:param str? multiline: long description 5,\ndefaults to 'bye'"

    def parse(text: T.Optional[str]) -> Docstring:
        """Parse the ReST-style docstring into its components.
    
        :returns: parsed docstring
        """
        ret = Docstring(style=DocstringStyle.REST)
        if not text:
            return ret
    
        text = inspect.cleandoc(text)
        match = re.search("^:", text, flags=re.M)
        if match:
            desc_chunk = text[: match.start()]
            meta_chunk = text[match.start() :]
        else:
            desc_chunk = text
            meta_chunk = ""
    
        parts = desc_chunk.split("\n", 1)
        ret.short_description = parts[0] or None
        if len(parts) > 1:
            long_desc_chunk = parts[1] or ""
            ret.blank_after_short_description = long_desc_chunk.startswith("\n")
            ret.blank_after_long_description = long_desc_chunk.endswith("\n\n")
            ret.long_description = long_desc_chunk.strip() or None
    
        types = {}
        rtypes = {}
        for match in re.finditer(
            r"(^:.*?)(?=^:|\Z)", meta_chunk, flags=re.S | re.M
        ):
            chunk = match.group(0)
            if not chunk:
                continue
            try:
>               args_chunk, desc_chunk = chunk.lstrip(":").split(":", 1)
E               ValueError: not enough values to unpack (expected 2, got 1)

docstring_parser/docstring_parser/rest.py:137: ValueError

The above exception was the direct cause of the following exception:

    def test_invalid_inputs() -> None:
        """Test invalid inputs to check error handling."""
        # Test with an empty docstring
        docstring = parse("")
        assert len(docstring.params) == 0
    
        # Test with a malformed docstring (missing colon after parameter name)
>       docstring = parse(
            """
            Short description
    
            :param name description 1
            :param int priority: description 2
            :param str? sender: description 3
            :param str? message: description 4, defaults to 'hello'
            :param str? multiline: long description 5,
            defaults to 'bye'
            """
        )

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_6_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = "Short description\n\n:param name description 1\n:param int priority: description 2\n:param str? sender: description 3\n:param str? message: description 4, defaults to 'hello'\n:param str? multiline: long description 5,\ndefaults to 'bye'"

    def parse(text: T.Optional[str]) -> Docstring:
        """Parse the ReST-style docstring into its components.
    
        :returns: parsed docstring
        """
        ret = Docstring(style=DocstringStyle.REST)
        if not text:
            return ret
    
        text = inspect.cleandoc(text)
        match = re.search("^:", text, flags=re.M)
        if match:
            desc_chunk = text[: match.start()]
            meta_chunk = text[match.start() :]
        else:
            desc_chunk = text
            meta_chunk = ""
    
        parts = desc_chunk.split("\n", 1)
        ret.short_description = parts[0] or None
        if len(parts) > 1:
            long_desc_chunk = parts[1] or ""
            ret.blank_after_short_description = long_desc_chunk.startswith("\n")
            ret.blank_after_long_description = long_desc_chunk.endswith("\n\n")
            ret.long_description = long_desc_chunk.strip() or None
    
        types = {}
        rtypes = {}
        for match in re.finditer(
            r"(^:.*?)(?=^:|\Z)", meta_chunk, flags=re.S | re.M
        ):
            chunk = match.group(0)
            if not chunk:
                continue
            try:
                args_chunk, desc_chunk = chunk.lstrip(":").split(":", 1)
            except ValueError as ex:
>               raise ParseError(
                    f'Error parsing meta information near "{chunk}".'
                ) from ex
E               docstring_parser.common.ParseError: Error parsing meta information near ":param name description 1
E               ".

docstring_parser/docstring_parser/rest.py:139: ParseError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_params_6_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.05s ===============================
"""