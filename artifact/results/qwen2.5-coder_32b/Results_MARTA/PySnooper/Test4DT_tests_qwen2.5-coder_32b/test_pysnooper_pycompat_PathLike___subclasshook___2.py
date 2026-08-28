
import pytest
from pysnooper.pycompat import PathLike

def test_instance_of_subclass_with_fspath_method():
    class MyPathClass(PathLike):
        def __fspath__(self) -> str:
            return '/some/path'

    my_path = MyPathClass()
    assert isinstance(my_path, PathLike)
    assert issubclass(MyPathClass, PathLike)


def test_non_conforming_subclass():
    class NonConformingPath:
        def open(self):
            pass

        @property
        def path(self) -> str:
            return '/non/conforming/path'

    assert not isinstance(NonConformingPath(), PathLike)
    assert not issubclass(NonConformingPath, PathLike)

def test_subclass_with_fspath_and_open():
    class MixedPathClass(PathLike):
        def __fspath__(self) -> str:
            return '/mixed/path'

        def open(self):
            pass

    mixed_path = MixedPathClass()
    assert isinstance(mixed_path, PathLike)
    assert issubclass(MixedPathClass, PathLike)

def test_subclass_with_fspath_only():
    class FspathOnlyClass(PathLike):
        def __fspath__(self) -> str:
            return '/fspath/only/path'

    fspath_only = FspathOnlyClass()
    assert isinstance(fspath_only, PathLike)
    assert issubclass(FspathOnlyClass, PathLike)