
from docstring_parser import parse  # Importing the parse function from docstring_parser module

def test_parse_basic_docstring():
    docstring_text = """
    Short description of what the function does.

    Long description providing more details about the function's behavior.

    Parameters
    ----------
    param1 : int
        Description of `param1`.
    param2 : str, optional
        Description of `param2` (default is None).

    Returns
    -------
    result : bool
        Description of the returned value.
    """
    parsed_doc = parse(docstring_text)
    assert parsed_doc.short_description == "Short description of what the function does."
    assert parsed_doc.long_description == "Long description providing more details about the function's behavior."
    expected_meta = [
        ('param1', 'int\n    Description of `param1`.'),
        ('param2', 'str, optional\n    Description of `param2` (default is None).')
    ]