
import itertools
from pytest import raises
from tqdm.contrib.itertools import product

def test_valid_case():
    from tqdm import auto as tqdm_auto
    for combination in product([1, 2], ['a', 'b'], tqdm_class=tqdm_auto.tqdm):
        assert isinstance(combination, tuple)

def test_edge_case():
    for combination in product():
        assert combination == ()

def test_error_case():
    with raises(TypeError):
        for combination in product(1, 2):
            print(combination)
