
import pytest
from docstring_parser.rest import DocstringMeta, ParseError

# Assuming these constants and classes are defined in the module 'docstring_parser.rest'
PARAM_KEYWORDS = ["param1", "param2"]
RETURNS_KEYWORDS = ["return"]
YIELDS_KEYWORDS = ["yield"]
DEPRECATION_KEYWORDS = ["deprecated"]
RAISES_KEYWORDS = ["raises"]

# Mocking the DocstringParam, DocstringReturns, etc., classes as placeholders for actual implementations
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

def _build_meta(args: list, desc: str) -> DocstringMeta:
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
            raise ParseError(f"Expected one or two arguments for a {key} keyword.")

        match = re.match(r".*defaults to (.+)", desc, flags=re.DOTALL)
        default = match.group(1).rstrip(".") if match else None

        return DocstringParam(args=args, description=desc, arg_name=arg_name, type_name=type_name, is_optional=is_optional, default=default)

    if key in RETURNS_KEYWORDS | YIELDS_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(f"Expected one or no arguments for a {key} keyword.")

        return DocstringReturns(args=args, description=desc, type_name=type_name, is_generator=(key in YIELDS_KEYWORDS))

    if key in DEPRECATION_KEYWORDS:
        match = re.search(r"^(?P<version>v?((?:\d+)(?:\.[0-9a-z\.]+))) (?P<desc>.+)", desc, flags=re.I)
        return DocstringDeprecated(args=args, version=(match.group("version") if match else None), description=(match.group("desc") if match else desc))

    if key in RAISES_KEYWORDS:
        if len(args) == 2:
            type_name = args[1]
        elif len(args) == 1:
            type_name = None
        else:
            raise ParseError(f"Expected one or no arguments for a {key} keyword.")
        return DocstringRaises(args=args, description=desc, type_name=type_name)

    return DocstringMeta(args=args, description=desc)

# Test case to validate the _build_meta function with valid parameters and default values
def test_valid_case_param_with_default():
    args = ["param1", "int", "p1"]
    desc = "This is param1 which defaults to an integer."
    meta = _build_meta(args, desc)
    
    assert isinstance(meta, DocstringParam)
    assert meta.arg_name == "p1"
    assert meta.type_name == "int"
    assert not meta.is_optional
    assert meta.default == "an integer value as extracted from the description"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest__build_meta_0_test_valid_case_param_with_default
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_case_param_with_default.py:59:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_case_param_with_default.py:59:60: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_case_param_with_default.py:75:16: E0602: Undefined variable 're' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_case_param_with_default.py:75:98: E0602: Undefined variable 're' (undefined-variable)


"""