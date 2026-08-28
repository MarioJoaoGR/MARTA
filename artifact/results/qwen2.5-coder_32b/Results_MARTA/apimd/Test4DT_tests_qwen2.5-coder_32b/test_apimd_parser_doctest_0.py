
import pytest
from apimd.parser import doctest


def test_empty_string_input():
    """Test scenario where input is an empty string."""
    input_doc = ""
    expected_output = ""
    assert doctest(input_doc) == expected_output

def test_no_examples():
    """Test scenario where there are no examples in the docstring."""
    input_doc = "This is a docstring with no examples."
    expected_output = "This is a docstring with no examples."
    assert doctest(input_doc) == expected_output

def test_single_example():
    """Test scenario with a single example in the docstring."""
    input_doc = """Usage example:
>>> 1 + 2
3"""
    expected_output = """Usage example:
```python
>>> 1 + 2
```
3"""
    assert doctest(input_doc) == expected_output

def test_multiple_examples():
    """Test scenario with multiple examples in the docstring."""
    input_doc = """Multiple examples:
>>> 1 + 2
3
Another example:
>>> print("Hello, world!")
Hello, world!"""
    expected_output = """Multiple examples:
```python
>>> 1 + 2
```
3
Another example:
```python
>>> print("Hello, world!")
```
Hello, world!"""
    assert doctest(input_doc) == expected_output


def test_example_at_end():
    """Test scenario with an example at the end of the docstring."""
    input_doc = """Text before example.
>>> 2 * 2
4"""
    expected_output = """Text before example.
```python
>>> 2 * 2
```
4"""
    assert doctest(input_doc) == expected_output

def test_example_with_no_output():
    """Test scenario with an example that has no output."""
    input_doc = """Example with no output:
>>> pass"""
    expected_output = """Example with no output:
```python
>>> pass
```"""
    assert doctest(input_doc) == expected_output

def test_consecutive_examples():
    """Test scenario with consecutive examples in the docstring."""
    input_doc = """Consecutive examples:
>>> 1 + 2
3
>>> 4 + 5
9"""
    expected_output = """Consecutive examples:
```python
>>> 1 + 2
```
3
```python
>>> 4 + 5
```
9"""
    assert doctest(input_doc) == expected_output