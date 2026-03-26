
import ast
from isort.api import Config, DEFAULT_CONFIG, type_mapping
from isort.literal import LiteralParsingFailure, LiteralSortTypeMismatch, assignments
from isort.prettyprint import ISortPrettyPrinter

def assignment(code: str, sort_type: str, extension: str, config: Config = DEFAULT_CONFIG) -> str:
    """Sorts the literal present within the provided code against the provided sort type, returning the sorted representation of the source code.
    """
    if sort_type == "assignments":
        return assignments(code)
    if sort_type not in type_mapping:
        raise ValueError(
            "Trying to sort using an undefined sort_type. "
            f"Defined sort types are {', '.join(type_mapping.keys())}."
        )

    variable_name, literal = code.split("=")
    variable_name = variable_name.strip()
    literal = literal.lstrip()
    try:
        value = ast.literal_eval(literal)
    except Exception as error:
        raise LiteralParsingFailure(code, error)

    expected_type, sort_function = type_mapping[sort_type]
    if type(value) is not expected_type:
        raise LiteralSortTypeMismatch(type(value), expected_type)

    printer = ISortPrettyPrinter(config)
    sorted_value_code = f"{variable_name} = {sort_function(value, printer)}"
    if config.formatting_function:
        sorted_value_code = config.formatting_function(
            sorted_value_code, extension, config
        ).rstrip()

    sorted_value_code += code[len(code.rstrip()) :]
    return sorted_value_code

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_literal_assignment_0_test_edge_case
isort/Test4DT_tests/test_isort_literal_assignment_0_test_edge_case.py:3:0: E0611: No name 'type_mapping' in module 'isort.api' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_edge_case.py:5:0: E0401: Unable to import 'isort.prettyprint' (import-error)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_edge_case.py:5:0: E0611: No name 'prettyprint' in module 'isort' (no-name-in-module)


"""