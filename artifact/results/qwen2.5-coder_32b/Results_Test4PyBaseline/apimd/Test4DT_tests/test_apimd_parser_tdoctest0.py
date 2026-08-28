
import pytest

def doctest(doc: str) -> str:
    """Wrap doctest as markdown Python code."""
    keep = False
    docs = []
    lines = doc.splitlines()
    for i, line in enumerate(lines):
        signed = line.startswith(">>> ")
        if signed:
            if not keep:
                docs.append("```python")
                keep = True
        elif keep:
            docs.append("```")
            keep = False
        docs.append(line)
        if signed and i == len(lines) - 1:
            docs.append("```")
            keep = False
    return '\n'.join(docs)

def test_doctest():
    input_doc = """Usage of the function:
>>> 2 + 2
4
This is a simple addition.
>>> print("Hello, world!")
Hello, world!
End of example."""
    formatted_doc = doctest(input_doc)
    expected_output = """Usage of the function:
```python
>>> 2 + 2
```
4
This is a simple addition.
```python
>>> print("Hello, world!")
```
Hello, world!
End of example."""
    assert formatted_doc == expected_output

def test_doctest_multiple_lines():
    input_doc = """Another example:
>>> for i in range(3):
...     print(i)
0
1
2
This demonstrates a loop."""
    formatted_doc = doctest(input_doc)
    expected_output = """Another example:
```python
>>> for i in range(3):
...     print(i)
```
0
1
2
This demonstrates a loop."""