
import pytest
from apimd.parser import Parser
from unittest.mock import patch, MagicMock

def test_valid_input_default_init():
    with patch('builtins.open', new=lambda x, y: open(x, 'r')):
        p = Parser()
        assert hasattr(p, 'link') and p.link is True
        assert hasattr(p, 'b_level') and p.b_level == 1
        assert hasattr(p, 'toc') and p.toc is False

