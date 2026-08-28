
import pytest
from pysnooper.pycompat import PathLike

class MyPathClass(PathLike):
    def __fspath__(self) -> str:
        return '/some/path'

class AnotherValidPathClass:
    def open(self):
        pass

    @property
    def path(self) -> str:
        return '/another/path'

class InvalidPathClass:
    def some_other_method(self):
        pass

def test_valid_case_with_fspath():
    assert issubclass(MyPathClass, PathLike)


def test_invalid_case_without_required_methods():
    assert not issubclass(InvalidPathClass, PathLike)