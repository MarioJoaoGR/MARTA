
import pytest
from tornado.options import OptionParser



def test_invalid_inputs():
    parser = OptionParser()
    with pytest.raises(AttributeError):
        parser.parse(['--invalid-option'])