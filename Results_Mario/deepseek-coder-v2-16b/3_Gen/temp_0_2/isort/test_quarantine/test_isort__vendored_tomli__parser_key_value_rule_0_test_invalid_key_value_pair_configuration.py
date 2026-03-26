
from isort._vendored.tomli._parser import parse_key_value_pair, suffixed_err, Flags

def key_value_rule(src: str, pos: int, out: Output, header: tuple, parse_float: ParseFloat) -> int:
    """Parses a key-value pair from the input string `src` starting at position `pos`. The function handles keys and values according to TOML specifications. It supports both bare keys and string literals (both single-quoted and double-quoted). After parsing the key, it expects an equal sign (`=`) followed by a value which is then parsed accordingly.

    Parameters:
        src (str): The input string or text from which to parse the key-value pair.
        pos (int): The current position in the source string where parsing should start or continue. This parameter must support indexing and incrementation.
        out (Output): An object that holds the parsed data and flags indicating whether certain keys are mutable or immutable.
        header (tuple): A nested tuple of strings representing the parent key namespace for the key-value pair being parsed.
        parse_float (ParseFloat): A callable function that converts string representations of floating-point numbers into actual float values.

    Returns:
        int: The updated position in the source string after parsing the key-value pair.

    Raises:
        suffixed_err: If the input string does not contain an equal sign (`=`) immediately following the key, if there is an invalid character in the key-value pair configuration, or if attempting to overwrite a value that has been frozen (immutable).
    """
    pos, key, value = parse_key_value_pair(src, pos, parse_float)
    key_parent, key_stem = key[:-1], key[-1]
    abs_key_parent = header + tuple(key_parent)

    if out.flags.is_(abs_key_parent, Flags.FROZEN):
        raise suffixed_err(src, pos, f"Can not mutate immutable namespace {abs_key_parent}")
    
    # Containers in the relative path can't be opened with the table syntax after this
    out.flags.set_for_relative_key(header, key, Flags.EXPLICIT_NEST)
    
    try:
        nest = out.data.get_or_create_nest(abs_key_parent)
    except KeyError:
        raise suffixed_err(src, pos, "Can not overwrite a value")
    
    if key_stem in nest:
        raise suffixed_err(src, pos, "Can not overwrite a value")
    
    # Mark inline table and array namespaces recursively immutable
    if isinstance(value, (dict, list)):
        out.flags.set(header + tuple(key), Flags.FROZEN, recursive=True)
    
    nest[key_stem] = value
    return pos

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_key_value_rule_0_test_invalid_key_value_pair_configuration
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_invalid_key_value_pair_configuration.py:4:44: E0602: Undefined variable 'Output' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_invalid_key_value_pair_configuration.py:4:80: E0602: Undefined variable 'ParseFloat' (undefined-variable)


"""