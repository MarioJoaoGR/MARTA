# Module: blib2to3.pgen2.grammar
import pytest
from blib2to3.pgen2.grammar import Grammar

# Test creating an instance of Grammar
def test_create_grammar():
    grammar = Grammar()
    assert isinstance(grammar, Grammar)
    assert grammar.symbol2number == {}
    assert grammar.number2symbol == {}
    assert grammar.states == []
    assert grammar.dfas == {}
    assert grammar.labels == [(0, "EMPTY")]
    assert grammar.keywords == {}
    assert grammar.tokens == {}
    assert grammar.symbol2label == {}
    assert grammar.start == 256
    assert not grammar.async_keywords

# Test copying a Grammar instance
def test_copy_grammar():
    grammar = Grammar()
    grammar_copy = grammar.copy()
    assert isinstance(grammar_copy, Grammar)
    assert grammar_copy.symbol2number == {}
    assert grammar_copy.number2symbol == {}
    assert grammar_copy.states == []
    assert grammar_copy.dfas == {}
    assert grammar_copy.labels == [(0, "EMPTY")]
    assert grammar_copy.keywords == {}
    assert grammar_copy.tokens == {}
    assert grammar_copy.symbol2label == {}
    assert grammar_copy.start == 256
    assert not grammar_copy.async_keywords

# Test that the copy is a deep copy and does not share references with the original
def test_deep_copy():
    grammar = Grammar()
    grammar_copy = grammar.copy()
    # Modify the original instance
    grammar.symbol2number["test"] = 256
    assert "test" not in grammar_copy.symbol2number

# Test that async_keywords is correctly copied
def test_async_keywords():
    grammar = Grammar()
    grammar_copy = grammar.copy()
    assert grammar_copy.async_keywords == grammar.async_keywords
