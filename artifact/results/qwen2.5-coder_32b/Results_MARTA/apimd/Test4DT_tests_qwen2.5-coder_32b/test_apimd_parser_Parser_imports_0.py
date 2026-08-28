
import pytest
from apimd.parser import Parser


def test_from_import():
    p = Parser()
    source_code = 'from os import path'
    p.parse('test_package', source_code)
    assert p.alias == {'test_package.path': 'os.path'}

def test_from_alias_import():
    p = Parser()
    source_code = 'from os import path as file_path'
    p.parse('test_package', source_code)
    assert p.alias == {'test_package.file_path': 'os.path'}