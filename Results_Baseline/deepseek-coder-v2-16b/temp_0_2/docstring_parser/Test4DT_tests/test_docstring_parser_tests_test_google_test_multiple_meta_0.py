
# Module: docstring_parser.tests.test_google
# Import the function using its module name
from docstring_parser.tests.test_google import test_multiple_meta

def test_parse():
    # Test parsing a Google-style docstring with multiple metadata entries
    from docstring_parser import parse  # Corrected the import and variable usage
    
    docstring = parse(
        """
        Short description

        Args:
            spam: asd
                1
                    2
                3

        Raises:
            bla: herp
            yay: derp
        """
    )
    
    # Assertions to check if the parsed docstring is correct
    assert docstring.short_description == "Short description"
    assert len(docstring.meta) == 3, f"Expected 3 metadata entries but got {len(docstring.meta)}"
    
    meta0 = docstring.meta[0]
    assert meta0.args == ["param", "spam"], f"Expected args to be ['param', 'spam'] but got {meta0.args}"
    assert meta0.arg_name == "spam", f"Expected arg_name to be 'spam' but got {meta0.arg_name}"
    assert meta0.description == "asd\n1\n    2\n3", f"Expected description to be 'asd\\n1\\n    2\\n3' but got '{meta0.description}'"
    
    meta1 = docstring.meta[1]
    assert meta1.args == ["raises", "bla"], f"Expected args to be ['raises', 'bla'] but got {meta1.args}"
    assert meta1.type_name == "bla", f"Expected type_name to be 'bla' but got {meta1.type_name}"
    assert meta1.description == "herp", f"Expected description to be 'herp' but got '{meta1.description}'"
    
    meta2 = docstring.meta[2]
    assert meta2.args == ["raises", "yay"], f"Expected args to be ['raises', 'yay'] but got {meta2.args}"
    assert meta2.type_name == "yay", f"Expected type_name to be 'yay' but got {meta2.type_name}"
    assert meta2.description == "derp", f"Expected description to be 'derp' but got '{meta2.description}'"
