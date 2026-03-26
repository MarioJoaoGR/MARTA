
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse  # Importing from the correct module name

def test_yields():
    """Test parsing yields."""
    # Call the function to get the docstring object
    docstring = parse(
        """
        Short description
        Yields
        ------
        int
            description
        """
    )
    
    # Assertions for meta items in the docstring
    assert len(docstring.meta) == 1, "Expected one meta item but got {}".format(len(docstring.meta))
    meta_item = docstring.meta[0]
    assert meta_item.args == ["yields"], "Expected argument 'yields' but got {}".format(meta_item.args)
    assert meta_item.type_name == "int", "Expected type 'int' but got '{}'".format(meta_item.type_name)
    assert meta_item.description == "description", "Expected description 'description' but got '{}'".format(meta_item.description)
    assert meta_item.return_name is None, "Expected return name to be None but got '{}'".format(meta_item.return_name)
    assert meta_item.is_generator, "Expected the item to be a generator but it is not"
