
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse  # Importing from the correct module name
import pytest

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

# Additional test case for handling different types of yields
def test_yields_different_type():
    """Test parsing yields with a different type."""
    docstring = parse(
        """
        Short description
        Yields
        ------
        float
            description
        """
    )
    
    assert len(docstring.meta) == 1, "Expected one meta item but got {}".format(len(docstring.meta))
    meta_item = docstring.meta[0]
    assert meta_item.args == ["yields"], "Expected argument 'yields' but got {}".format(meta_item.args)
    assert meta_item.type_name == "float", "Expected type 'float' but got '{}'".format(meta_item.type_name)
    assert meta_item.description == "description", "Expected description 'description' but got '{}'".format(meta_item.description)
    assert meta_item.return_name is None, "Expected return name to be None but got '{}'".format(meta_item.return_name)
    assert meta_item.is_generator, "Expected the item to be a generator but it is not"

# Additional test case for handling no yields in docstring
def test_yields_no_yields():
    """Test parsing without any yields."""
    docstring = parse(
        """
        Short description
        """
    )
    
    assert len(docstring.meta) == 0, "Expected zero meta items but got {}".format(len(docstring.meta))

# Additional test case for handling multiple yields in docstring
def test_yields_multiple():
    """Test parsing with multiple yields."""
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
    
    assert len(docstring.meta) == 2, "Expected two meta items but got {}".format(len(docstring.meta))
    assert docstring.meta[0].args == ["yields"], "Expected argument 'yields' for the first item but got {}".format(docstring.meta[0].args)
    assert docstring.meta[0].type_name == "int", "Expected type 'int' for the first item but got '{}'".format(docstring.meta[0].type_name)
    assert docstring.meta[0].description == "description1", "Expected description 'description1' for the first item but got '{}'".format(docstring.meta[0].description)
    assert docstring.meta[0].return_name is None, "Expected return name to be None for the first item but got '{}'".format(docstring.meta[0].return_name)
    assert docstring.meta[0].is_generator, "Expected the first item to be a generator but it is not"
    
    assert docstring.meta[1].args == ["yields"], "Expected argument 'yields' for the second item but got {}".format(docstring.meta[1].args)
    assert docstring.meta[1].type_name == "float", "Expected type 'float' for the second item but got '{}'".format(docstring.meta[1].type_name)
    assert docstring.meta[1].description == "description2", "Expected description 'description2' for the second item but got '{}'".format(docstring.meta[1].description)
    assert docstring.meta[1].return_name is None, "Expected return name to be None for the second item but got '{}'".format(docstring.meta[1].return_name)
    assert docstring.meta[1].is_generator, "Expected the second item to be a generator but it is not"

# Additional test case for handling empty yields in docstring
def test_yields_empty():
    """Test parsing with empty yields."""
    docstring = parse(
        """
        Short description
        Yields
        ------
        """
    )
    
    assert len(docstring.meta) == 0, "Expected zero meta items but got {}".format(len(docstring.meta))

# Additional test case for handling yields with additional content in docstring
def test_yields_with_additional_content():
    """Test parsing yields with additional content."""
    docstring = parse(
        """
        Short description
        Some other section
        Yields
        ------
        int
            description
        """
    )
    
    assert len(docstring.meta) == 1, "Expected one meta item but got {}".format(len(docstring.meta))
    meta_item = docstring.meta[0]
    assert meta_item.args == ["yields"], "Expected argument 'yields' but got {}".format(meta_item.args)
    assert meta_item.type_name == "int", "Expected type 'int' but got '{}'".format(meta_item.type_name)
    assert meta_item.description == "description", "Expected description 'description' but got '{}'".format(meta_item.description)
    assert meta_item.return_name is None, "Expected return name to be None but got '{}'".format(meta_item.return_name)
    assert meta_item.is_generator, "Expected the item to be a generator but it is not"
