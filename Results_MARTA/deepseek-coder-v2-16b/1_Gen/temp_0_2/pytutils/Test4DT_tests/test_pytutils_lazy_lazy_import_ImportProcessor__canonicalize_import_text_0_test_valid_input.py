
from pytutils.lazy.lazy_import import ImportProcessor, lazy_import

def test_canonicalize_import_text():
    processor = ImportProcessor()
    
    # Test with a simple import statement
    text = '''
    from os import path
    from sys import argv
    '''
    
    expected_output = [
        'from os import path',
        'from sys import argv'
    ]
    
    assert processor._canonicalize_import_text(text) == expected_output
