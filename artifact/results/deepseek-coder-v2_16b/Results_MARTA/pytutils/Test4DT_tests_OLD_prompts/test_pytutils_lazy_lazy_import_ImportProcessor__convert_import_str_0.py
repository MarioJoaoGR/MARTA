
import pytest
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

# Test default import processor
def test_default_import_processor():
    processor = ImportProcessor()
    text = "from math import sqrt"
    with pytest.raises(ValueError) as excinfo:
        processor._convert_import_str(text)
    assert str(excinfo.value) == 'bad import string %r' % (text,)

# Test custom lazy import processor
def test_custom_lazy_import_processor():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    with pytest.raises(ValueError) as excinfo:
        processor._convert_import_str(text)
    assert str(excinfo.value) == 'bad import string %r' % (text,)

# Test process import statements

# Test specific module path
def test_specific_module_path():
    class CustomLazyImport(ImportReplacer):
        def replace_import(self, module_name):
            return f"lazy_import('{module_name}')"
    
    processor = ImportProcessor(CustomLazyImport)
    text = "from math import sqrt"
    with pytest.raises(ValueError) as excinfo:
        processor._convert_import_str(text)
    assert str(excinfo.value) == 'bad import string %r' % (text,)