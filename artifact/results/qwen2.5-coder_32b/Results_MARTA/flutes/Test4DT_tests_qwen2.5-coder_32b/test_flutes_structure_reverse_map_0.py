
import pytest
from typing import Dict, List
from flutes.structure import reverse_map

def test_reverse_map_with_words():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    id_to_word = reverse_map(word_to_id)
    assert id_to_word == words

def test_reverse_map_with_numbers():
    numbers = [10, 20, 30]
    number_to_id = {num: idx for idx, num in enumerate(numbers)}
    id_to_number = reverse_map(number_to_id)
    assert id_to_number == numbers

def test_reverse_map_with_mixed_types():
    mixed_items = ['apple', 42, 3.14]
    mixed_to_id = {item: idx for idx, item in enumerate(mixed_items)}
    id_to_mixed = reverse_map(mixed_to_id)
    assert id_to_mixed == mixed_items

def test_reverse_map_with_custom_objects():
    class Item:
        def __init__(self, name):
            self.name = name

    items = [Item('item1'), Item('item2'), Item('item3')]
    item_to_id = {item: idx for idx, item in enumerate(items)}
    id_to_item = reverse_map(item_to_id)
    assert [item.name for item in id_to_item] == ['item1', 'item2', 'item3']
