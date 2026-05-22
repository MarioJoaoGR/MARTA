
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.requestitems import KeyValueArg, process_data_embed_raw_json_file_arg

@pytest.fixture
def setup_keyvaluearg():
    return KeyValueArg(key="test_key", value="test_value", sep='=', orig='test_orig')

def test_none_input(setup_keyvaluearg):
    with patch('httpie.cli.requestitems.load_text_file', return_value=None):
        with patch('httpie.cli.requestitems.load_json', side_effect=ValueError("Invalid JSON")):
            with pytest.raises(ValueError) as excinfo:
                process_data_embed_raw_json_file_arg(setup_keyvaluearg)
            assert str(excinfo.value) == "Invalid JSON"
