
import pytest
from collections.abc import Mapping, Sequence

# Assuming these classes are defined as shown in your example
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


# SampleObject class for testing
class SampleObject:
    def __init__(self):
        self.attribute_name = "value"
        self.other_attr = 42


# Test cases
def test_happy_path_list():
    expl = Exploding(source="x + y")
    list_input = [10, 20, 30]
    assert expl._items(list_input) == [10, 20, 30]






def test_edge_case_empty_dict():
    expl = Exploding(source="x + y")
    empty_dict = {}
    assert expl._items(empty_dict) == []


def test_edge_case_empty_list():
    expl = Exploding(source="x + y")
    empty_list = []
    assert expl._items(empty_list) == []


def test_edge_case_single_item_list():
    expl = Exploding(source="x + y")
    single_item_list = [42]
    assert expl._items(single_item_list) == [42]







