
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.swfinterp import _AVMClass, _AVMClass_Object

def test_make_object():
    with patch('youtube_dl.swfinterp._AVMClass_Object', autospec=True) as mock_avm_class_object:
        avm_class = _AVMClass(name_idx=1, name='MyClass', static_properties={'prop1': 'value1'})
        methods = {'method1': 0, 'method2': 1}
        avm_class.register_methods(methods)
        avm_object = avm_class.make_object()
        assert isinstance(mock_avm_class_object.return_value, _AVMClass_Object)
        assert isinstance(avm_object, _AVMClass_Object)


def test_make_object_with_mocked_dependencies():
    with patch('youtube_dl.swfinterp._AVMClass_Object', autospec=True) as mock_avm_class_object:
        avm_class = _AVMClass(name_idx=1, name='MyClass', static_properties={'prop1': 'value1'})
        methods = {'method1': 0, 'method2': 1}
        avm_class.register_methods(methods)
        avm_object = avm_class.make_object()
        assert isinstance(mock_avm_class_object.return_value, _AVMClass_Object)
        assert isinstance(avm_object, _AVMClass_Object)