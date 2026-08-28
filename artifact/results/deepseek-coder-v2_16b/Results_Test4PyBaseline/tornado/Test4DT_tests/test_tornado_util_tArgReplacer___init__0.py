
# Module: tornado.util
import pytest
from unittest.mock import patch, MagicMock
from typing import Callable, Optional
from tornado.util import ArgReplacer

# Mock function for testing purposes
def example_function(a, b=2):
    pass

class TestArgReplacer:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.func = example_function
        self.arg_replacer = ArgReplacer(self.func, 'b')
    
    def test_init_with_valid_argument(self):
        assert self.arg_replacer.name == 'b'