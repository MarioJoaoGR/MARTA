
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

class TestImportProcessorCanonicalizeImportTextInvalidInput:
    def test_invalid_input(self):
        processor = ImportProcessor()
        try:
            processor._canonicalize_import_text("invalid input")
        except Exception as e:
            assert isinstance(e, ValueError)
