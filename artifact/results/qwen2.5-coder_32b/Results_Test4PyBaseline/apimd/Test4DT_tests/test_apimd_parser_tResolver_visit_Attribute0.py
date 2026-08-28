# Module: apimd.parser
import pytest
from ast import Attribute, Name, Load
from apimd.parser import Resolver

def test_resolver_initialization():
    # Test initialization with required parameters
    resolver = Resolver(root='my_module', alias={'np': 'numpy'})
    assert resolver.root == 'my_module'
    assert resolver.alias == {'np': 'numpy'}
    assert resolver.self_ty == ""

    # Test initialization with all parameters
    resolver = Resolver(root='my_module', alias={'np': 'numpy'}, self_ty='MyClass')
    assert resolver.root == 'my_module'
    assert resolver.alias == {'np': 'numpy'}
    assert resolver.self_ty == 'MyClass'

def test_visit_attribute_typing_prefix():
    # Create an Attribute node representing 'typing.List'
    attribute_node = Attribute(
        value=Name(id='typing', ctx=Load()),
        attr='List',
        ctx=Load()
    )
    
    resolver = Resolver(root='my_module', alias={'np': 'numpy'})
    cleaned_attribute_node = resolver.visit_Attribute(attribute_node)
    
    # Assert that the node is now a Name node with id 'List'
    assert isinstance(cleaned_attribute_node, Name)
    assert cleaned_attribute_node.id == 'List'

def test_visit_attribute_no_typing_prefix():
    # Create an Attribute node representing 'math.sqrt'
    attribute_node = Attribute(
        value=Name(id='math', ctx=Load()),
        attr='sqrt',
        ctx=Load()
    )
    
    resolver = Resolver(root='my_module', alias={'np': 'numpy'})
    unchanged_attribute_node = resolver.visit_Attribute(attribute_node)
    
    # Assert that the node remains unchanged
    assert isinstance(unchanged_attribute_node, Attribute)
    assert unchanged_attribute_node.value.id == 'math'
    assert unchanged_attribute_node.attr == 'sqrt'

def test_visit_attribute_non_name_value():
    # Create an Attribute node with a non-Name value
    attribute_node = Attribute(
        value=Attribute(value=Name(id='typing', ctx=Load()), attr='List', ctx=Load()),
        attr='append',
        ctx=Load()
    )
    
    resolver = Resolver(root='my_module', alias={'np': 'numpy'})
    unchanged_attribute_node = resolver.visit_Attribute(attribute_node)
    
    # Assert that the node remains unchanged
    assert isinstance(unchanged_attribute_node, Attribute)

def test_visit_attribute_empty_alias():
    # Create an Attribute node representing 'typing.List'
    attribute_node = Attribute(
        value=Name(id='typing', ctx=Load()),
        attr='List',
        ctx=Load()
    )
    
    resolver = Resolver(root='my_module', alias={})
    cleaned_attribute_node = resolver.visit_Attribute(attribute_node)
    
    # Assert that the node is now a Name node with id 'List'
    assert isinstance(cleaned_attribute_node, Name)
    assert cleaned_attribute_node.id == 'List'

def test_visit_attribute_with_self_ty():
    # Create an Attribute node representing 'typing.List'
    attribute_node = Attribute(
        value=Name(id='typing', ctx=Load()),
        attr='List',
        ctx=Load()
    )
    
    resolver = Resolver(root='my_module', alias={'np': 'numpy'}, self_ty='MyClass')
    cleaned_attribute_node = resolver.visit_Attribute(attribute_node)
    
    # Assert that the node is now a Name node with id 'List'
    assert isinstance(cleaned_attribute_node, Name)
    assert cleaned_attribute_node.id == 'List'
