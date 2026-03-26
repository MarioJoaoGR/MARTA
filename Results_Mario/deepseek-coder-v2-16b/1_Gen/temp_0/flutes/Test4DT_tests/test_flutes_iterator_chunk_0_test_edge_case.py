
import pytest
from typing import Iterable, List, Iterator, TypeVar

T = TypeVar('T')

def chunk(n: int, iterable: Iterable[T]) -> Iterator[List[T]]:
    r"""Split the iterable into chunks, with each chunk containing no more than ``n`` elements.

    .. code:: python

        >>> list(chunk(3, range(10)))
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

    :param n: The maximum number of elements in one chunk.
    :param iterable: The iterable.
    :return: An iterator over chunks.
    """
    if n <= 0:
        raise ValueError("`n` should be positive")
    group = []
    for x in iterable:
        group.append(x)
        if len(group) == n:
            yield group
            group = []
    if len(group) > 0:
        yield group

def test_edge_case():
    n = 3
    iterable = None
    with pytest.raises(TypeError):
        list(chunk(n, iterable))
