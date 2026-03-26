
# Module: docstring_parser.tests.test_google
import pytest
from googleparser import parse

def test_params():
    """Tests the parsing of parameters in a Google-style docstring."""
    
    # Test with no parameters
    docstring = parse("Short description")
    assert len(docstring.params) == 0, "Expected 0 parameters but got {}".format(len(docstring.params))

    # Test with multiple parameters
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4, "Expected 4 parameters but got {}".format(len(docstring.params))
    assert docstring.params[0].arg_name == "name", "Expected arg_name 'name' but got '{}'".format(docstring.params[0].arg_name)
    assert docstring.params[0].type_name is None, "Expected type_name to be None for 'name' but got '{}'".format(docstring.params[0].type_name)
    assert docstring.params[0].description == "description 1", "Expected description 'description 1' for 'name' but got '{}'".format(docstring.params[0].description)
    assert not docstring.params[0].is_optional, "Expected 'name' to be non-optional but it is optional"
    assert docstring.params[1].arg_name == "priority", "Expected arg_name 'priority' but got '{}'".format(docstring.params[1].arg_name)
    assert docstring.params[1].type_name == "int", "Expected type_name 'int' for 'priority' but got '{}'".format(docstring.params[1].type_name)
    assert docstring.params[1].description == "description 2", "Expected description 'description 2' for 'priority' but got '{}'".format(docstring.params[1].description)
    assert not docstring.params[1].is_optional, "Expected 'priority' to be non-optional but it is optional"
    assert docstring.params[2].arg_name == "sender", "Expected arg_name 'sender' but got '{}'".format(docstring.params[2].arg_name)
    assert docstring.params[2].type_name == "str", "Expected type_name 'str' for 'sender' but got '{}'".format(docstring.params[2].type_name)
    assert docstring.params[2].description == "description 3", "Expected description 'description 3' for 'sender' but got '{}'".format(docstring.params[2].description)
    assert docstring.params[2].is_optional, "Expected 'sender' to be optional but it is not"
    assert docstring.params[3].arg_name == "ratio", "Expected arg_name 'ratio' but got '{}'".format(docstring.params[3].arg_name)
    assert docstring.params[3].type_name == "Optional[float]", "Expected type_name 'Optional[float]' for 'ratio' but got '{}'".format(docstring.params[3].type_name)
    assert docstring.params[3].description == "description 4", "Expected description 'description 4' for 'ratio' but got '{}'".format(docstring.params[3].description)
    assert docstring.params[3].is_optional, "Expected 'ratio' to be optional but it is not"

    # Test with multi-line descriptions in parameters
    docstring = parse(
        """
        Short description

        Args:
            name: description 1
                with multi-line text
            priority (int): description 2
        """
    )
    assert len(docstring.params) == 2, "Expected 2 parameters but got {}".format(len(docstring.params))
    assert docstring.params[0].arg_name == "name", "Expected arg_name 'name' but got '{}'".format(docstring.params[0].arg_name)
    assert docstring.params[0].type_name is None, "Expected type_name to be None for 'name' but got '{}'".format(docstring.params[0].type_name)
    assert docstring.params[0].description == (
        "description 1\nwith multi-line text"
    ), "Expected description 'description 1 with multi-line text' for 'name' but got '{}'".format(docstring.params[0].description)
    assert not docstring.params[0].is_optional, "Expected 'name' to be non-optional but it is optional"
    assert docstring.params[1].arg_name == "priority", "Expected arg_name 'priority' but got '{}'".format(docstring.params[1].arg_name)
    assert docstring.params[1].type_name == "int", "Expected type_name 'int' for 'priority' but got '{}'".format(docstring.params[1].type_name)
    assert docstring.params[1].description == "description 2", "Expected description 'description 2' for 'priority' but got '{}'".format(docstring.params[1].description)
    assert not docstring.params[1].is_optional, "Expected 'priority' to be non-optional but it is optional"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_google_test_params_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_params_0.py:4:0: E0401: Unable to import 'googleparser' (import-error)

"""