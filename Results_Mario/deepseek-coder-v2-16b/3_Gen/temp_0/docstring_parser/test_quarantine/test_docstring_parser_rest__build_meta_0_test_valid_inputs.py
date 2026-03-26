
import pytest
from docstring_parser.rest import DocstringMeta, ParseError
from typing import List as TList

# Assuming the following imports are needed for the function to work correctly
import re

PARAM_KEYWORDS = ["param"]
RETURNS_KEYWORDS = ["return"]
YIELDS_KEYWORDS = ["yield"]
DEPRECATION_KEYWORDS = ["deprecated"]
RAISES_KEYWORDS = ["raises"]

class DocstringParam(DocstringMeta):
    pass

class DocstringReturns(DocstringMeta):
    pass

class DocstringDeprecated(DocstringMeta):
    pass

class DocstringRaises(DocstringMeta):
    pass

def _build_meta(args: TList[str], desc: str) -> DocstringMeta:
    key = args[0]

    if key in PARAM_KEYWORDS:
        if len(args) == 3:
            key, type_name, arg_name = args
            if type_name.endswith("?"):
                is_optional = True
                type_name = type_name[:-1]
            else:
                is_optional = False
        elif len(args) == 2:
            key, arg_name = args
            type_name = None
            is_optional = None
        else:
            raise ParseError(
                f"Expected one or two arguments for a {key} keyword."
            )

        match = re.match(r".*defaults to (.+)", desc, flags=re.DOTALL)
        default = match.group(1).rstrip(".") if match else None

        return DocstringParam(
            args=args,
            description=desc,
            arg_name=arg_name,
            type_name=type_name,
            is_optional=is_optional,
            default=default,
        )

    if key in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(
                f"Expected one or no arguments for a {key} keyword."
            )

        return DocstringReturns(
            args=args,
            description=desc,
            type_name=type_name,
            is_generator=key in YIELDS_KEYWORDS,
        )

    if key in DEPRECATION_KEYWORDS:
        match = re.search(
            r"^(?P<version>v?((?:\d+)(?:\.[0-9a-z\.]+))) (?P<desc>.+)",
            desc,
            flags=re.I,
        )
        return DocstringDeprecated(
            args=args,
            version=match.group("version") if match else None,
            description=match.group("desc") if match else desc,
        )

    if key in RAISES_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(
                f"Expected one or no arguments for a {key} keyword."
            )
        return DocstringRaises(
            args=args, description=desc, type_name=type_name
        )

    return DocstringMeta(args=args, description=desc)

# Test case to validate the function with valid inputs
def test_valid_inputs():
    # Test for parameter meta information
    meta = _build_meta(args=["param1", "int", "example_arg"], desc="This parameter is used to set up the example.")
    assert meta.args == ["param1", "int", "example_arg"]
    assert meta.description == "This parameter is used to set up the example."
    assert meta.arg_name == "example_arg"
    assert meta.type_name == "int"
    assert meta.is_optional is False
    assert meta.default is None

    # Test for return meta information
    meta = _build_meta(args=["return"], desc="This function returns a value.")
    assert meta.args == ["return"]
    assert meta.description == "This function returns a value."
    assert meta.type_name is None
    assert not meta.is_generator

    # Test for deprecated meta information
    meta = _build_meta(args=["deprecated", "v1.0"], desc="Deprecated since version 1.0.")
    assert meta.args == ["deprecated", "v1.0"]
    assert meta.description == "Deprecated since version 1.0."
    assert meta.version == "v1.0"

    # Test for raises meta information
    meta = _build_meta(args=["raises", "ValueError"], desc="This function may raise a ValueError.")
    assert meta.args == ["raises", "ValueError"]
    assert meta.description == "This function may raise a ValueError."
    assert meta.type_name == "ValueError"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:50:15: E1123: Unexpected keyword argument 'arg_name' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:50:15: E1123: Unexpected keyword argument 'type_name' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:50:15: E1123: Unexpected keyword argument 'is_optional' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:50:15: E1123: Unexpected keyword argument 'default' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:69:15: E1123: Unexpected keyword argument 'type_name' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:69:15: E1123: Unexpected keyword argument 'is_generator' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:82:15: E1123: Unexpected keyword argument 'version' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:97:15: E1123: Unexpected keyword argument 'type_name' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:109:11: E1101: Instance of 'DocstringMeta' has no 'arg_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:109:11: E1101: Instance of 'DocstringReturns' has no 'arg_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:109:11: E1101: Instance of 'DocstringDeprecated' has no 'arg_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:109:11: E1101: Instance of 'DocstringParam' has no 'arg_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:109:11: E1101: Instance of 'DocstringRaises' has no 'arg_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:110:11: E1101: Instance of 'DocstringMeta' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:110:11: E1101: Instance of 'DocstringReturns' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:110:11: E1101: Instance of 'DocstringDeprecated' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:110:11: E1101: Instance of 'DocstringParam' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:110:11: E1101: Instance of 'DocstringRaises' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:111:11: E1101: Instance of 'DocstringMeta' has no 'is_optional' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:111:11: E1101: Instance of 'DocstringReturns' has no 'is_optional' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:111:11: E1101: Instance of 'DocstringDeprecated' has no 'is_optional' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:111:11: E1101: Instance of 'DocstringParam' has no 'is_optional' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:111:11: E1101: Instance of 'DocstringRaises' has no 'is_optional' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:112:11: E1101: Instance of 'DocstringMeta' has no 'default' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:112:11: E1101: Instance of 'DocstringReturns' has no 'default' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:112:11: E1101: Instance of 'DocstringDeprecated' has no 'default' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:112:11: E1101: Instance of 'DocstringParam' has no 'default' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:112:11: E1101: Instance of 'DocstringRaises' has no 'default' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:118:11: E1101: Instance of 'DocstringMeta' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:118:11: E1101: Instance of 'DocstringRaises' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:118:11: E1101: Instance of 'DocstringParam' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:118:11: E1101: Instance of 'DocstringDeprecated' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:118:11: E1101: Instance of 'DocstringReturns' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:119:15: E1101: Instance of 'DocstringMeta' has no 'is_generator' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:119:15: E1101: Instance of 'DocstringRaises' has no 'is_generator' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:119:15: E1101: Instance of 'DocstringParam' has no 'is_generator' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:119:15: E1101: Instance of 'DocstringDeprecated' has no 'is_generator' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:119:15: E1101: Instance of 'DocstringReturns' has no 'is_generator' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:125:11: E1101: Instance of 'DocstringReturns' has no 'version' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:125:11: E1101: Instance of 'DocstringParam' has no 'version' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:125:11: E1101: Instance of 'DocstringMeta' has no 'version' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:125:11: E1101: Instance of 'DocstringDeprecated' has no 'version' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:125:11: E1101: Instance of 'DocstringRaises' has no 'version' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:131:11: E1101: Instance of 'DocstringReturns' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:131:11: E1101: Instance of 'DocstringMeta' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:131:11: E1101: Instance of 'DocstringDeprecated' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:131:11: E1101: Instance of 'DocstringParam' has no 'type_name' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:131:11: E1101: Instance of 'DocstringRaises' has no 'type_name' member (no-member)


"""