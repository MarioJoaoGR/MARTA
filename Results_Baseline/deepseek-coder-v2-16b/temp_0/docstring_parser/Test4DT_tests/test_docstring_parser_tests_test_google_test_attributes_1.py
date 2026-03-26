
# Module: docstring_parser.tests.test_google
from docstring_parser.tests.test_google import parse

def test_attributes():
    # Test case for empty docstring
    docstring = parse("Short description")
    assert len(docstring.params) == 0, "Expected no parameters but got some"

    # Additional test cases to cover uncovered lines
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
            priority (int): description 2
            sender (str?): description 3
            ratio (Optional[float], optional): description 4
        """
    )
    assert len(docstring.params) == 4, "Expected four parameters but got fewer"
    assert docstring.params[0].arg_name == "name", f"Expected 'name' but got {docstring.params[0].arg_name}"
    assert docstring.params[0].type_name is None, "Expected no type for name"
    assert docstring.params[0].description == "description 1", f"Expected description 1 but got {docstring.params[0].description}"
    assert not docstring.params[0].is_optional, "Name should not be optional"
    assert docstring.params[1].arg_name == "priority", f"Expected 'priority' but got {docstring.params[1].arg_name}"
    assert docstring.params[1].type_name == "int", f"Expected type int for priority but got {docstring.params[1].type_name}"
    assert docstring.params[1].description == "description 2", f"Expected description 2 but got {docstring.params[1].description}"
    assert not docstring.params[1].is_optional, "Priority should not be optional"
    assert docstring.params[2].arg_name == "sender", f"Expected 'sender' but got {docstring.params[2].arg_name}"
    assert docstring.params[2].type_name == "str", f"Expected type str for sender but got {docstring.params[2].type_name}"
    assert docstring.params[2].description == "description 3", f"Expected description 3 but got {docstring.params[2].description}"
    assert docstring.params[2].is_optional, "Sender should be optional"
    assert docstring.params[3].arg_name == "ratio", f"Expected 'ratio' but got {docstring.params[3].arg_name}"
    assert docstring.params[3].type_name == "Optional[float]", f"Expected type Optional[float] for ratio but got {docstring.params[3].type_name}"
    assert docstring.params[3].description == "description 4", f"Expected description 4 but got {docstring.params[3].description}"
    assert docstring.params[3].is_optional, "Ratio should be optional"

    # Test case for multi-line descriptions within attributes
    docstring = parse(
        """
        Short description

        Attributes:
            name: description 1
                with multi-line text
            priority (int): description 2
        """
    )
    assert len(docstring.params) == 2, "Expected two parameters but got fewer"
    assert docstring.params[0].arg_name == "name", f"Expected 'name' but got {docstring.params[0].arg_name}"
    assert docstring.params[0].type_name is None, "Expected no type for name"
    assert docstring.params[0].description == (
        "description 1\nwith multi-line text"
    ), f"Expected combined description but got {docstring.params[0].description}"
    assert not docstring.params[0].is_optional, "Name should not be optional"
    assert docstring.params[1].arg_name == "priority", f"Expected 'priority' but got {docstring.params[1].arg_name}"
    assert docstring.params[1].type_name == "int", f"Expected type int for priority but got {docstring.params[1].type_name}"
    assert docstring.params[1].description == "description 2", f"Expected description 2 but got {docstring.params[1].description}"
    assert not docstring.params[1].is_optional, "Priority should not be optional"
