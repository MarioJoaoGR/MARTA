
import pytest
from blib2to3.pgen2.grammar import Grammar

# Test initialization of the Grammar class
def test_init():
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

# Test copying the Grammar class instance
def test_copy():
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
    assert grammar_copy is not grammar

# Test that the copy method creates a deep copy
def test_deep_copy():
    grammar = Grammar()
    grammar.symbol2number["test"] = 257
    grammar.number2symbol[257] = "test"
    grammar.dfas[0] = ([(0, [("test", 0)])], {1})
    grammar.keywords["async"] = 1
    grammar.tokens[1] = "ASYNC"
    grammar.symbol2label["test"] = 1
    grammar.start = 257
    grammar.async_keywords = True

    grammar_copy = grammar.copy()
    assert grammar_copy.symbol2number == {"test": 257}
    assert grammar_copy.number2symbol == {257: "test"}