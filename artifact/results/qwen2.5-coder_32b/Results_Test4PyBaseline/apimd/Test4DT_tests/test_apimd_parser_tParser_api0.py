
import pytest
from apimd.parser import Parser
from ast import FunctionDef, AsyncFunctionDef, ClassDef, parse

def create_function_node(name: str):
    return FunctionDef(
        name=name,
        args=parse("def foo(): pass").body[0].args,
        body=[],
        decorator_list=[],
        returns=None
    )

def create_async_function_node(name: str):
    return AsyncFunctionDef(
        name=name,
        args=parse("async def foo(): pass").body[0].args,
        body=[],
        decorator_list=[],
        returns=None
    )

def create_class_node(name: str):
    return ClassDef(
        name=name,
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[]
    )

def test_api_with_function_def():
    p = Parser()
    node = create_function_node('test_func')
    p.level['example_package'] = 1  # Initialize the level for the root module
    p.api('example_package', node)
    assert 'example_package.test_func' in p.doc