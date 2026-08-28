
import pytest
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

# Example 1: Using Default ImportReplacer
def test_default_import_processor():
    processor = ImportProcessor()
    text = "from math import sqrt"
    with pytest.raises(ValueError):
        processor._convert_import_str(text)

# Example 2: Using Custom Lazy Import Replacement Logic
class CustomLazyImport(ImportReplacer):
    def replace_import(self, module_name):
        return f"lazy_import('{module_name}')"

def test_custom_lazy_import_processor():
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    with pytest.raises(ValueError):
        processor._convert_import_str(text)

# Example 3: Processing Text with Import Statements
def test_process_import_statements():
    processor = ImportProcessor()
    try:
        text = "import foo, foo.bar, foo.bar.baz as bing"
        processor._convert_import_str(text)
    except ValueError as e:
        assert str(e) == 'bad import string %r' % (text,)

# Example 4: Handling Import Statements with Spaces and Aliases
def test_handle_imports_with_spaces_and_aliases():
    processor = ImportProcessor()
    try:
        text = "from math import sqrt, cos"
        processor._convert_import_str(text)
    except ValueError as e:
        assert str(e) == 'bad import string %r' % (text,)

# Example 5: Using ImportProcessor with a Specific Module Path
def test_specific_module_path():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"

    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    with pytest.raises(ValueError):
        processor._convert_import_str(text)
