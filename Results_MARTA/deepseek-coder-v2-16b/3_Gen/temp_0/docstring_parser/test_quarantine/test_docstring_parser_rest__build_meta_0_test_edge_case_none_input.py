
import pytest
from docstring_parser.rest import DocstringMeta, ParseError
from typing import List as TList

# Assuming these are defined elsewhere in your module or imported from another file
PARAM_KEYWORDS = ["param"]
RETURNS_KEYWORDS = ["return"]
YIELDS_KEYWORDS = ["yield"]
DEPRECATION_KEYWORDS = ["deprecated"]
RAISES_KEYWORDS = ["raise"]

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

# Test case to check the edge case where input is None
def test_edge_case_none_input():
    with pytest.raises(TypeError):
        _build_meta(args=None, desc="This should raise a TypeError")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_edge_case_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:33:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:33:60: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:36:15: E0602: Undefined variable 'DocstringParam' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:55:15: E0602: Undefined variable 'DocstringReturns' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:63:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:66:18: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:68:15: E0602: Undefined variable 'DocstringDeprecated' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_case_none_input.py:83:15: E0602: Undefined variable 'DocstringRaises' (undefined-variable)


"""