
import pytest
from unittest.mock import patch, MagicMock
from typing import Iterable, Callable, Optional, Any

class LazyChoices:
    def __init__(
        self,
        *args,
        getter: Callable[[], Iterable[Any]],
        help_formatter: Optional[Callable[[Any, bool], str]] = None,
        sort: bool = False,
        cache: bool = True,
        isolation_mode: bool = False,
        **kwargs
    ) -> None:
        self.getter = getter
        self.help_formatter = help_formatter
        self.sort = sort
        self.cache = cache
        self.isolation_mode = isolation_mode
        self._help: Optional[str] = None
        self._obj: Optional[Iterable[Any]] = None
        super().__init__(*args, **kwargs)
        self.choices = self

    def load(self) -> Iterable[Any]:
        if self._obj is None or not self.cache:
            self._obj = self.getter()
            if self.sort:
                self._obj = sorted(self._obj)
        return self._obj

    def __contains__(self, item: Any) -> bool:
        return item in self.load()

@pytest.fixture
def valid_choices():
    return LazyChoices(getter=lambda: [1, 2, 3], sort=True, cache=False)

def test_valid_inputs(valid_choices):
    assert list(valid_choices.load()) == [1, 2, 3]
