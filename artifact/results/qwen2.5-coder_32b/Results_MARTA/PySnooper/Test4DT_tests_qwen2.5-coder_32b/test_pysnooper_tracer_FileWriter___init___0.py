
import pytest
from pysnooper.tracer import FileWriter

def test_filewriter_init_with_overwrite():
    # Test initialization with overwrite set to True
    path = 'testfile.txt'
    overwrite = True
    writer = FileWriter(path, overwrite)
    assert writer.path == path
    assert writer.overwrite == overwrite

def test_filewriter_init_without_overwrite():
    # Test initialization with overwrite set to False
    path = 'testfile.txt'
    overwrite = False
    writer = FileWriter(path, overwrite)
    assert writer.path == path
    assert writer.overwrite == overwrite

def test_filewriter_init_with_absolute_path():
    # Test initialization with an absolute path
    import os
    path = os.path.abspath('testfile.txt')
    overwrite = True
    writer = FileWriter(path, overwrite)
    assert writer.path == path
    assert writer.overwrite == overwrite

def test_filewriter_init_with_pathlike_object():
    # Test initialization with a PathLike object
    from pathlib import Path
    path_obj = Path('testfile.txt')
    overwrite = False
    writer = FileWriter(path_obj, overwrite)
    assert writer.path == str(path_obj)
    assert writer.overwrite == overwrite
