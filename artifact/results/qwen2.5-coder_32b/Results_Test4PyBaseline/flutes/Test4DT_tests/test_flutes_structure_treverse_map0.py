
import pytest
from flutes.structure import reverse_map
from typing import Dict, List

def test_reverse_map_basic_usage():
    words = ['a', 'aardvark', 'abandon']
    word_to_id = {word: idx for idx, word in enumerate(words)}
    assert reverse_map(word_to_id) == ['a', 'aardvark', 'abandon']

def test_reverse_map_with_integers():
    numbers = [10, 20, 30]
    number_to_id = {num: idx for idx, num in enumerate(numbers)}
    assert reverse_map(number_to_id) == [10, 20, 30]

def test_reverse_map_custom_ids():
    custom_ids = {'apple': 2, 'banana': 0, 'cherry': 1}
    assert reverse_map(custom_ids) == ['banana', 'cherry', 'apple']

def test_reverse_map_empty_dict():
    empty_dict: Dict[str, int] = {}
    assert reverse_map(empty_dict) == []

def test_reverse_map_single_element():
    single_element = {'only': 0}
    assert reverse_map(single_element) == ['only']

def test_reverse_map_out_of_order_ids():
    out_of_order_ids = {'first': 2, 'second': 1, 'third': 0}
    assert reverse_map(out_of_order_ids) == ['third', 'second', 'first']

def test_reverse_map_large_numbers():
    large_numbers = {f'item_{i}': i for i in range(100)}
    assert reverse_map(large_numbers) == [f'item_{i}' for i in range(100)]

def test_reverse_map_negative_ids():
    negative_ids = {'a': -1, 'b': 0}
    # Assuming the function does not raise an error and handles negative indices gracefully
    result = reverse_map(negative_ids)
    assert len(result) == 2