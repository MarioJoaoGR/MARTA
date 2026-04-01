
from isort.output import _LineWithComments  # Correctly specify the module and class name

def test_valid_input():
    value = "example"
    comments = ["This is a comment.", "Another comment."]
    line = _LineWithComments(value, comments)
    
    assert isinstance(line, _LineWithComments), "The instance should be an instance of _LineWithComments"
    assert line.comments == comments, "The comments in the instance should match the provided comments"
