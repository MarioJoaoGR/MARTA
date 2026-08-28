
import pytest
from apimd.parser import Parser







def test_private_module_name():
    p = Parser()
    # Assuming '_private.module.name' starts with an underscore and should be considered private
    p.imp['_private'] = {'module'}
    p.root['_private.module.name'] = '_private'
    assert p.is_public('_private.module.name') is False


def test_nested_private_module_name():
    p = Parser()
    # Assuming '_private.module.submodule' starts with an underscore and should be considered private
    p.imp['_private'] = {'module'}
    p.root['_private.module.submodule'] = '_private'
    assert p.is_public('_private.module.submodule') is False

