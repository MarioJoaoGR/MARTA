
import pytest
from pysnooper.pycompat import PathLike

class MyPath(PathLike):
    def __init__(self, path: str):
        self._path = path

    def __fspath__(self) -> str:
        return self._path

class AnotherPathClass:
    def open(self):
        pass

    @property
    def path(self) -> str:
        return '/another/path'

def test_valid_case_with_fspath():
    assert issubclass(MyPath, PathLike)

def test_invalid_case_without_fspath_or_open_and_path_in_name():
    class InvalidPath:
        def some_method(self):
            pass

    assert not issubclass(InvalidPath, PathLike)

def test_valid_case_with_open_and_path_in_name():
    class AnotherPathClassWithOpenAndPathInName(PathLike):
        def open(self):
            pass

        @property
        def path(self) -> str:
            return '/another/path'

    assert issubclass(AnotherPathClassWithOpenAndPathInName, PathLike)

def test_invalid_case_with_open_but_no_path_in_name():
    class AnotherPathWithoutPathInName:
        def open(self):
            pass

    assert not issubclass(AnotherPathWithoutPathInName, PathLike)
