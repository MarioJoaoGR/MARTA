
from pytutils.lazy.lazy_import import ImportReplacer

class TestImportReplacer:
    def test_error_case_invalid_inputs(self):
        # Arrange
        scope = {}
        name = 'test_module'
        module_path = ['test_module']
        member = None
        children = {'child': (['test_module', 'child'], None, {})}
        
        # Act and Assert
        try:
            ImportReplacer(scope, name, module_path, member, children)
        except ValueError as e:
            assert str(e) == 'Cannot supply both a member and children'
