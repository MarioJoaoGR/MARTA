
import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin:
    @pytest.fixture(autouse=True)
    def setup_plugin(self):
        self.converter = ConverterPlugin('application/custom-mime')

    def test_convert_not_implemented(self):
        with pytest.raises(NotImplementedError):
            self.converter.convert(b'some binary data')
