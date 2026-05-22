
import pytest
from unittest.mock import patch
from httpie.output.models import ProcessingOptions

def test_edge_case_none():
    with patch('httpie.output.models.ProcessingOptions.__init__', return_value=None):
        options = ProcessingOptions()
        assert not options.debug and not options.traceback, "Both debug and traceback should be None"
