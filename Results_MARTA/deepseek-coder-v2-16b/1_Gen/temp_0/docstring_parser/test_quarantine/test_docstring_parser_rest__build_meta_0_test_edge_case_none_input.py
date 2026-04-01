
import pytest
from docstring_parser.rest import DocstringMeta, ParseError
from typing import List as TList

# Assuming these are defined somewhere in your module or standard library
PARAM_KEYWORDS = ["param"]
RETURNS_KEYWORDS = ["return"]
YIELDS_KEYWORDS = ["yield"]
DEPRECATION_KEYWORDS = ["deprecated"]
RAISES_KEYWORDS = ["raise"]

# Mocking DocstringParam, DocstringReturns, DocstringDeprecated, and DocstringRaises for the example
class DocstringParam:
    def __init__(self, args, description, arg_name, type_name, is_optional, default):
        self.args = args
        self.description = description
        self.arg_name = arg_name
        self.type_name = type_name
        self.is_optional = is_optional
        self.default = default

class DocstringReturns:
    def __init__(self, args, description, type_name, is_generator):
        self.args = args
        self.description = description
        self.type_name = type_name
        self.is_generator = is_generator

class DocstringDeprecated:
    def __init__(self, args, version, description):
        self.args = args
        self.version = version
        self.description = description

class DocstringRaises:
    def __init__(self, args, description, type_name):
        self.args = args
        self.description = description
        self.type_name = type_name

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

# Test case to check the edge case where no input is provided
def test_edge_case_none_input():
    with pytest.raises(ParseError):
        meta = _build_meta([], "This should raise an error because there's no key.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_edge_case_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:62:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:62:60: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:92:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:95:18: E0602: Undefined variable 're' (undefined-variable)

"""