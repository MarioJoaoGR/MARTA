
import pytest
from blib2to3.pgen2.grammar import Grammar

def test_init():
    grammar = Grammar()
    assert isinstance(grammar.symbol2number, dict)
    assert isinstance(grammar.number2symbol, dict)
    assert isinstance(grammar.states, list)
    assert isinstance(grammar.dfas, dict)
    assert isinstance(grammar.labels, list)
    assert isinstance(grammar.keywords, dict)
    assert isinstance(grammar.tokens, dict)
    assert isinstance(grammar.symbol2label, dict)
    assert grammar.start == 256
    assert not grammar.async_keywords

@pytest.mark.xfail(reason="Method is expected to raise NotImplementedError")
def test_load():
    grammar = Grammar()
    with pytest.raises(NotImplementedError):
        grammar.load("path/to/pickle/file")

@pytest.mark.xfail(reason="Method is expected to raise NotImplementedError")
def test_dump():
    grammar = Grammar()
    with pytest.raises(NotImplementedError):
        grammar.dump("path/to/another/pickle/file")

@pytest.mark.xfail(reason="Method is expected to raise NotImplementedError")
def test_report():
    grammar = Grammar()
    with pytest.raises(NotImplementedError):
        grammar.report()

@pytest.mark.xfail(reason="Method is expected to raise NotImplementedError")
def test_copy():
    grammar = Grammar()
    with pytest.raises(NotImplementedError):
        copy_of_grammar = grammar.copy()
