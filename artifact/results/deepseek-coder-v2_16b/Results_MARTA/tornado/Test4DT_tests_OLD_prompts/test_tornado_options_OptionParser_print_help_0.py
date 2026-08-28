
import pytest
from unittest.mock import patch
from tornado.options import OptionParser, Error

def test_valid_inputs():
    parser = OptionParser()
    with patch('tornado.options.OptionParser._normalize_name', return_value='help'):
        with pytest.raises(Error):
            parser.define("help", type=bool, help="show this help information", callback=parser._help_callback)

