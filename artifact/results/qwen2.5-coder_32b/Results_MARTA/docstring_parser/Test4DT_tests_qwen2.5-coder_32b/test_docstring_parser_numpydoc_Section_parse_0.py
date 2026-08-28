
import inspect
from docstring_parser.numpydoc import Section, DocstringMeta

def test_edge_cases_empty_text():
    section = Section("Parameters", "param")
    text = ''
    meta_items = list(section.parse(text))
    assert len(meta_items) == 1
    assert meta_items[0].description is None





def test_no_description():
    section = Section("Parameters", "param")
    text = inspect.cleandoc('''
        x : int
    ''')
    meta_items = list(section.parse(text))
    assert len(meta_items) == 1
    assert meta_items[0].description.strip() == 'x : int'

