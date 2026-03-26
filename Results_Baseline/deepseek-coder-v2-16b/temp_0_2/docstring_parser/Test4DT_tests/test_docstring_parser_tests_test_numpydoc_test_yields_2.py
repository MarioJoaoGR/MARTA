
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse  # Importing from the correct module name

def test_yields():
    """Test parsing yields."""
    # Test case for short description and yield metadata
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

def test_yields_no_description():
    """Test parsing yields without description."""
    # Test case for short description and yield metadata without description
    docstring = parse(
        """
        Short description
        Yields
        ------
        int
        """
    )
    
    # Assertions for meta items in the docstring
    assert len(docstring.meta) == 1, "Expected one meta item but got {}".format(len(docstring.meta))
    meta_item = docstring.meta[0]
    assert meta_item.args == ["yields"], "Expected argument 'yields' but got {}".format(meta_item.args)
    assert meta_item.type_name == "int", "Expected type 'int' but got '{}'".format(meta_item.type_name)
    assert meta_item.description is None, "Expected description to be None but got '{}'".format(meta_item.description)
    assert meta_item.return_name is None, "Expected return name to be None but got '{}'".format(meta_item.return_name)
    assert meta_item.is_generator, "Expected the item to be a generator but it is not"

def test_yields_multiple_entries():
    """Test parsing multiple metadata entries."""
    # Test case for short description and two yield metadata entries
    docstring = parse(
        """
        Short description
        Yields
        ------
        int
            description1
        float
            description2
        """
    )
    
    # Assertions for meta items in the docstring
    assert len(docstring.meta) == 2, "Expected two meta items but got {}".format(len(docstring.meta))
    assert docstring.meta[0].args == ["yields"], "First argument should be 'yields' but got {}".format(docstring.meta[0].args)
    assert docstring.meta[0].type_name == "int", "First type should be 'int' but got '{}'".format(docstring.meta[0].type_name)
    assert docstring.meta[0].description == "description1", "First description should be 'description1' but got '{}'".format(docstring.meta[0].description)
    assert docstring.meta[0].return_name is None, "First return name should be None but got '{}'".format(docstring.meta[0].return_name)
    assert docstring.meta[0].is_generator, "First item should be a generator but it is not"
    
    assert docstring.meta[1].args == ["yields"], "Second argument should be 'yields' but got {}".format(docstring.meta[1].args)
    assert docstring.meta[1].type_name == "float", "Second type should be 'float' but got '{}'".format(docstring.meta[1].type_name)
    assert docstring.meta[1].description == "description2", "Second description should be 'description2' but got '{}'".format(docstring.meta[1].description)
    assert docstring.meta[1].return_name is None, "Second return name should be None but got '{}'".format(docstring.meta[1].return_name)
    assert docstring.meta[1].is_generator, "Second item should be a generator but it is not"
