
from pytutils.lazy.lazy_import import ImportReplacer

class TestImportReplacer:
    def test_invalid_input_error_handling(self):
        # Test that an error is raised when both member and children are provided
        try:
            ImportReplacer(scope=globals(), name='foo', module_path=['foo'], member='bar', children={'baz': (['foo', 'baz'], None, {})})
            assert False, "Expected ValueError but no exception was raised"
        except ValueError as e:
            assert str(e) == 'Cannot supply both a member and children', f"Unexpected error message: {str(e)}"
