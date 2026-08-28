# Module: blib2to3.pgen2.grammar
import pytest
from blib2to3.pgen2.grammar import Grammar

# Test creating an instance of the Grammar class
def test_create_grammar_instance():
    grammar = Grammar()
    assert isinstance(grammar, Grammar), "Expected an instance of Grammar"
    assert hasattr(grammar, 'symbol2number'), "Expected symbol2number attribute to be present"
    assert hasattr(grammar, 'number2symbol'), "Expected number2symbol attribute to be present"
    assert hasattr(grammar, 'states'), "Expected states attribute to be present"
    assert hasattr(grammar, 'dfas'), "Expected dfas attribute to be present"
    assert hasattr(grammar, 'labels'), "Expected labels attribute to be present"
    assert hasattr(grammar, 'keywords'), "Expected keywords attribute to be present"
    assert hasattr(grammar, 'tokens'), "Expected tokens attribute to be present"
    assert hasattr(grammar, 'symbol2label'), "Expected symbol2label attribute to be present"
    assert hasattr(grammar, 'start'), "Expected start attribute to be present"
    assert hasattr(grammar, 'async_keywords'), "Expected async_keywords attribute to be present"

# Test the report method of the Grammar class
def test_report_method():
    grammar = Grammar()
    # Since the report method prints to stdout, we can't directly check its output.
    # Instead, we will check if it runs without errors and that it has printed something relevant.
    import io
    from contextlib import redirect_stdout
    
    f = io.StringIO()
    with redirect_stdout(f):
        grammar.report()
    output = f.getvalue().strip()
    
    assert "s2n" in output, "Expected 's2n' to be printed"
    assert "n2s" in output, "Expected 'n2s' to be printed"
    assert "states" in output, "Expected 'states' to be printed"
    assert "dfas" in output, "Expected 'dfas' to be printed"
    assert "labels" in output, "Expected 'labels' to be printed"
    assert "start 256" in output, "Expected 'start 256' to be printed"
