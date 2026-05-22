
import pytest
from httpie.cli.options import Argument

class TestArgumentGetattr:
    def setUp(self):
        self.arg = Argument()
        self.arg.configuration = {'key1': 'value1', 'key2': 'value2'}

    def test_none_input(self):
        with pytest.raises(AttributeError):
            assert self.arg.nonExistentKey is None
