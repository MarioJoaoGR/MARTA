
import unittest
from httpie.output.ui.rich_palette import _GenericColorCaster

class TestHttpieOutputUiRichPalette__GenericColorCasterGet1TestCase(unittest.TestCase):
    def test_none_input(self):
        color_caster = _GenericColorCaster()
        result = color_caster.get(None)
        self.assertIsNone(result)
