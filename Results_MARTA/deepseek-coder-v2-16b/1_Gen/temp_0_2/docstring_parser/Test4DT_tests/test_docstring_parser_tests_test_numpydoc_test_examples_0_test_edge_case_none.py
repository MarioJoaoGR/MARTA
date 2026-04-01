
import pytest
from docstring_parser.tests.test_numpydoc import parse
import typing as T

@pytest.mark.parametrize("source, expected_results", [
    (None, [])
])
def test_examples(
    source, expected_results: T.List[T.Tuple[T.Optional[str], str]]
) -> None:
    """Test parsing examples by comparing the parsed results with the provided expected results."""
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results)
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1]
    assert len(docstring.examples) == len(expected_results)
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0]
        assert example.description == expected_result[1]
