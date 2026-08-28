
from docstring_parser.google import GoogleParser, Section, DocstringParam

def test_build_multi_meta_param():
    parser = GoogleParser()
    param_section = Section(title="Parameters", key="param", type="multiple")
    meta_param = parser._build_multi_meta(param_section, 'x: int, optional', 'The x coordinate.')
    assert isinstance(meta_param, DocstringParam)