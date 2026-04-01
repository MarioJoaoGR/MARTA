
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

def test_invalid_input():
    processor = ImportProcessor()
    
    # Test with invalid input that does not start with 'import'
    try:
        processor._convert_import_str('foo bar')
        assert False, "Expected ValueError but no exception was raised"
    except ValueError as e:
        assert str(e) == 'bad import string %r' % ('foo bar',), f"Unexpected error message: {str(e)}"
