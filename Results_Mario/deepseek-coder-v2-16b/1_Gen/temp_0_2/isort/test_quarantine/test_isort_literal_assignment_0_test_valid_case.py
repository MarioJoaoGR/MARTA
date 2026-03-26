
import ast
from isort import sort_literal, type_mapping, assignments, prettyprint
from isort.sorting import DEFAULT_CONFIG, ISortPrettyPrinter
from isort.exceptions import LiteralParsingFailure, LiteralSortTypeMismatch

def assignment(code: str, sort_type: str, extension: str, config: Config = DEFAULT_CONFIG) -> str:
    """Sorts the literal present within the provided code against the provided sort type,
    returning the sorted representation of the source code.
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
************* Module Test4DT_tests.test_isort_literal_assignment_0_test_valid_case
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:3:0: E0611: No name 'sort_literal' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:3:0: E0611: No name 'type_mapping' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:3:0: E0611: No name 'assignments' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:3:0: E0611: No name 'prettyprint' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:4:0: E0611: No name 'DEFAULT_CONFIG' in module 'isort.sorting' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:4:0: E0611: No name 'ISortPrettyPrinter' in module 'isort.sorting' (no-name-in-module)
isort/Test4DT_tests/test_isort_literal_assignment_0_test_valid_case.py:7:66: E0602: Undefined variable 'Config' (undefined-variable)


"""