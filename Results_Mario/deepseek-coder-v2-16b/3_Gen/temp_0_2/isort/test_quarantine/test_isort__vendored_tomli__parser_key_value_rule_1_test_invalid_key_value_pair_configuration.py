
def test_invalid_key_value_pair_configuration():
    src = "invalid=format"
    pos = 0
    out = Output()
    header = ()
    parse_float = float
    
    try:
        new_pos = key_value_rule(src, pos, out, header, parse_float)
    except ValueError as e:
        assert str(e) == "Can not mutate immutable namespace ()"
    else:
        raise AssertionError("Expected a ValueError but got no exception")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_key_value_rule_1_test_invalid_key_value_pair_configuration
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_1_test_invalid_key_value_pair_configuration.py:5:10: E0602: Undefined variable 'Output' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_1_test_invalid_key_value_pair_configuration.py:10:18: E0602: Undefined variable 'key_value_rule' (undefined-variable)


"""