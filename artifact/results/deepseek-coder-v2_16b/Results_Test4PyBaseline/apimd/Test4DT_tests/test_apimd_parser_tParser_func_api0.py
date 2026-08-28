
# Module: apimd.parser
import pytest
from apimd.parser import Parser

# Assuming 'parsed_content' is an instance of the appropriate class for arguments
parsed_content = None  # Corrected to match the assumption in the test case
returns = None
has_self = True
cls_method = False

def test_func_api():
    parser = Parser()
    with pytest.raises(AttributeError):
        parser.func_api(root='mypackage', name='myfunction', node=parsed_content, returns=returns, has_self=has_self, cls_method=cls_method)
