
import unittest.mock as mock
from httpie.output.processing import Conversion, ConverterPlugin, plugin_manager

def test_none_input():
    conversion = Conversion()
    with mock.patch('httpie.output.processing.plugin_manager.get_converters') as get_converters_mock:
        get_converters_mock.return_value = []
        result = conversion.get_converter("invalid/mime")
        assert result is None
