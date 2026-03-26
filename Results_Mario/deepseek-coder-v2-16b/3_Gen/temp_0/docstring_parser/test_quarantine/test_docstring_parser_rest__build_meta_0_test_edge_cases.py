
import re
from docstring_parser.rest import DocstringMeta, ParseError, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DEPRECATION_KEYWORDS, RAISES_KEYWORDS
from typing import List as TList

def _build_meta(args: TList[str], desc: str) -> DocstringMeta:
    """
    Constructs a `DocstringMeta` object based on the provided arguments and description.
    
    This function interprets the type of metadata indicated by the first argument (`key`) and processes it accordingly, whether it's for parameters, returns, deprecations, or raises. It handles both single and multiple argument scenarios to parse keyword-based docstring meta information.

    Parameters:
        args (List[str]): A list containing strings that identify the type of metadata being described. The first element is typically used as a key to determine the kind of meta information (e.g., parameter, return).
        desc (str): A string description accompanying the arguments, providing detailed information about what the function does or how it operates.

    Returns:
        DocstringMeta: An instance of `DocstringMeta` containing the parsed metadata from the provided arguments and description.

    Raises:
        ParseError: If the number of arguments is incorrect for the specified keyword, an error is raised with a message indicating the expected format.

    Examples:
        >>> meta = _build_meta(args=["param1", "int", "example_arg"], desc="This parameter is used to set up the example.")
        >>> print(meta.args)  # Output: ['param1', 'int', 'example_arg']
        >>> print(meta.description)  # Output: This parameter is used to set up the example.
        >>> print(meta.arg_name)  # Output: example_arg
        >>> print(meta.type_name)  # Output: int
        >>> print(meta.is_optional)  # Output: False (assuming not optional based on provided args)
        >>> print(meta.default)  # Output: None (assuming no default value)
        
        This example demonstrates how to use the function with a parameter meta information, showing how you can access and print various attributes of the returned `DocstringMeta` object.
    """
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_cases.py:55:15: E0602: Undefined variable 'DocstringParam' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_cases.py:74:15: E0602: Undefined variable 'DocstringReturns' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_cases.py:87:15: E0602: Undefined variable 'DocstringDeprecated' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_edge_cases.py:102:15: E0602: Undefined variable 'DocstringRaises' (undefined-variable)


"""