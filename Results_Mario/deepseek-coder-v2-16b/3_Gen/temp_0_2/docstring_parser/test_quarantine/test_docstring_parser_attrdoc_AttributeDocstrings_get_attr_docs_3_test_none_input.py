
import pytest
import ast
import inspect
import textwrap
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.visitor = AttributeDocstrings()
    
    @pytest.mark.parametrize("component", [None, object(), type('TestClass', (), {})])
    def test_none_input(self, component):
        result = self.visitor.get_attr_docs(component)
        assert result == {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
________________ TestAttributeDocstrings.test_none_input[None] _________________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.TestAttributeDocstrings object at 0x103055540>
component = None

    @pytest.mark.parametrize("component", [None, object(), type('TestClass', (), {})])
    def test_none_input(self, component):
>       result = self.visitor.get_attr_docs(component)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/attrdoc.py:90: in get_attr_docs
    source = textwrap.dedent(inspect.getsource(component))
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:1139: in getsource
    lines, lnum = getsourcelines(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:1121: in getsourcelines
    lines, lnum = findsource(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:940: in findsource
    file = getsourcefile(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:817: in getsourcefile
    filename = getfile(object)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

object = None

    def getfile(object):
        """Work out which source or compiled file an object was defined in."""
        if ismodule(object):
            if getattr(object, '__file__', None):
                return object.__file__
            raise TypeError('{!r} is a built-in module'.format(object))
        if isclass(object):
            if hasattr(object, '__module__'):
                module = sys.modules.get(object.__module__)
                if getattr(module, '__file__', None):
                    return module.__file__
                if object.__module__ == '__main__':
                    raise OSError('source code not available')
            raise TypeError('{!r} is a built-in class'.format(object))
        if ismethod(object):
            object = object.__func__
        if isfunction(object):
            object = object.__code__
        if istraceback(object):
            object = object.tb_frame
        if isframe(object):
            object = object.f_code
        if iscode(object):
            return object.co_filename
>       raise TypeError('module, class, method, function, traceback, frame, or '
                        'code object was expected, got {}'.format(
                        type(object).__name__))
E       TypeError: module, class, method, function, traceback, frame, or code object was expected, got NoneType

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:797: TypeError
_____________ TestAttributeDocstrings.test_none_input[component1] ______________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.TestAttributeDocstrings object at 0x103055720>
component = <object object at 0x1013bde10>

    @pytest.mark.parametrize("component", [None, object(), type('TestClass', (), {})])
    def test_none_input(self, component):
>       result = self.visitor.get_attr_docs(component)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
docstring_parser/docstring_parser/attrdoc.py:90: in get_attr_docs
    source = textwrap.dedent(inspect.getsource(component))
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:1139: in getsource
    lines, lnum = getsourcelines(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:1121: in getsourcelines
    lines, lnum = findsource(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:940: in findsource
    file = getsourcefile(object)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:817: in getsourcefile
    filename = getfile(object)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

object = <object object at 0x1013bde10>

    def getfile(object):
        """Work out which source or compiled file an object was defined in."""
        if ismodule(object):
            if getattr(object, '__file__', None):
                return object.__file__
            raise TypeError('{!r} is a built-in module'.format(object))
        if isclass(object):
            if hasattr(object, '__module__'):
                module = sys.modules.get(object.__module__)
                if getattr(module, '__file__', None):
                    return module.__file__
                if object.__module__ == '__main__':
                    raise OSError('source code not available')
            raise TypeError('{!r} is a built-in class'.format(object))
        if ismethod(object):
            object = object.__func__
        if isfunction(object):
            object = object.__code__
        if istraceback(object):
            object = object.tb_frame
        if isframe(object):
            object = object.f_code
        if iscode(object):
            return object.co_filename
>       raise TypeError('module, class, method, function, traceback, frame, or '
                        'code object was expected, got {}'.format(
                        type(object).__name__))
E       TypeError: module, class, method, function, traceback, frame, or code object was expected, got object

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/inspect.py:797: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.py::TestAttributeDocstrings::test_none_input[None]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_3_test_none_input.py::TestAttributeDocstrings::test_none_input[component1]
========================= 2 failed, 1 passed in 0.13s ==========================
"""