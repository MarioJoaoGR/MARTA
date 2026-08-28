
import pytest
from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json.core import _decode_items

@dataclass
class Point:
    x: int
    y: int

def test_decode_items_dataclass():
    points = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
    decoded_points = list(_decode_items(Point, points, infer_missing=False))
    assert decoded_points == [Point(x=1, y=2), Point(x=3, y=4)]

def test_decode_items_optional():
    optional_ints = [1, None, 3]
    decoded_optional_ints = list(_decode_items(Optional[int], optional_ints, infer_missing=True))
    assert decoded_optional_ints == [1, None, 3]

def test_decode_items_generics():
    int_list = [[1, 2, 3], [4, 5]]
    decoded_int_lists = list(_decode_items(List[int], int_list, infer_missing=False))
    assert decoded_int_lists == [[1, 2, 3], [4, 5]]

def test_decode_items_infer_missing_false():
    points_with_missing = [{'x': 1}, {'y': 2}]
    with pytest.raises(KeyError):
        list(_decode_items(Point, points_with_missing, infer_missing=False))

def test_decode_items_infer_missing_true():
    points_with_missing = [{'x': 1}, {'y': 2}]
    decoded_points = list(_decode_items(Point, points_with_missing, infer_missing=True))
    # Assuming default values are set to None or some other default
    assert decoded_points == [Point(x=1, y=None), Point(x=None, y=2)]

def test_decode_items_empty_list():
    empty_list = []
    decoded_empty_list = list(_decode_items(Point, empty_list, infer_missing=False))