
import pytest
from collections.abc import Mapping, Sequence
from pysnooper.variables import Exploding

# Assuming Keys, Indices, and Attrs classes are defined as shown in the analysis
class Keys:
    def __init__(self, source, exclude):
        self.source = source
        self.exclude = exclude

    def _items(self, main_value, normalize=False):
        items = [v for k, v in main_value.items() if k not in self.exclude]
        return items if not normalize else [str(v) for v in items]  # Example normalization


class Indices:
    def __init__(self, source, exclude):
        self.source = source
        self.exclude = exclude

    def _items(self, main_value, normalize=False):
        items = [main_value[i] for i in range(len(main_value)) if i not in self.exclude]
        return items if not normalize else [str(v) for v in items]  # Example normalization


class Attrs:
    def __init__(self, source, exclude):
        self.source = source
        self.exclude = exclude

    def _items(self, main_value, normalize=False):
        items = [getattr(main_value, attr) for attr in dir(main_value) if not callable(getattr(main_value, attr)) and attr not in self.exclude]
        return items if not normalize else [str(v) for v in items]  # Example normalization


# Extending the Exploding class to use the defined Keys, Indices, and Attrs
class Exploding:
    def __init__(self, source, exclude=None):
        self.source = source
        self.exclude = exclude or []

    def _items(self, main_value, normalize=False):
        if isinstance(main_value, Mapping):
            cls = Keys
        elif isinstance(main_value, Sequence):
            cls = Indices
        else:
            cls = Attrs

        return cls(self.source, self.exclude)._items(main_value, normalize)






def test_exploding_with_dict():
    expl = Exploding('x + y')
    assert expl._items({'a': 1, 'b': 2}) == [1, 2]


def test_exploding_with_dict_normalized():
    expl = Exploding('x + y')
    assert expl._items({'a': 1, 'b': 2}, normalize=True) == ["1", "2"]


def test_exploding_with_list():
    expl = Exploding('x + y')
    assert expl._items([10, 20, 30]) == [10, 20, 30]


def test_exploding_with_list_normalized():
    expl = Exploding('x + y')
    assert expl._items([10, 20, 30], normalize=True) == ["10", "20", "30"]

