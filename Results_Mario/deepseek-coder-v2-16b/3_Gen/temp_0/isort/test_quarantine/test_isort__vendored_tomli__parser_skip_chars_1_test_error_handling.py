
def skip_chars(src: str, pos: Pos, chars: Iterable[str]) -> Pos:
    try:
        while src[pos] in chars:
            pos += 1
    except IndexError:
        return pos
    return pos

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling.py:2:30: E0602: Undefined variable 'Pos' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling.py:2:42: E0602: Undefined variable 'Iterable' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_skip_chars_1_test_error_handling.py:2:60: E0602: Undefined variable 'Pos' (undefined-variable)


"""