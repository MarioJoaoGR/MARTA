
import pytest
from ansible.cli.doc import DocCLI

@pytest.fixture
def doccli():
    args = ['--list-modules']  # Example argument for testing initialization
    return DocCLI(args=args)

def test_init_with_args(doccli):
    assert isinstance(doccli, DocCLI), "Initialization with arguments should create an instance of DocCLI"

def test_get_keywords_docs():
    keys = ['keyword1', 'keyword2']  # Replace with actual keywords you want to test
    doccli = DocCLI(args=['--list-modules'])  # Assuming --list-modules is the correct argument for listing modules
    keywords_docs = doccli._get_keywords_docs(keys)
    assert isinstance(keywords_docs, dict), "The method should return a dictionary"