
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_edge_cases():
    parser = HTTPieArgumentParser()
    
    # Test None for self.args.prettify
    with pytest.raises(AttributeError):
        parser.args.prettify = None
