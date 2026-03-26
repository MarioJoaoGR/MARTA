
import ast
from isort import Config, DEFAULT_CONFIG, type_mapping, LiteralParsingFailure, LiteralSortTypeMismatch, ISortPrettyPrinter

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
************* Module Test4DT_tests.test_isort_literal_assignment_0_test_error_case
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:3:0: E0611: No name 'DEFAULT_CONFIG' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:3:0: E0611: No name 'type_mapping' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:3:0: E0611: No name 'LiteralParsingFailure' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:3:0: E0611: No name 'LiteralSortTypeMismatch' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:3:0: E0611: No name 'ISortPrettyPrinter' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_error_case.py:9:15: E0602: Undefined variable 'assignments' (undefined-variable)


"""