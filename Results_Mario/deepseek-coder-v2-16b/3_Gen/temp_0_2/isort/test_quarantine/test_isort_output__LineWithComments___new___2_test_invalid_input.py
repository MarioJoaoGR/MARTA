
class _LineWithComments:
    comments: list[str]
    
    def __new__(cls, value: Any, comments: list[str]) -> "_LineWithComments":
        if not isinstance(comments, list) or not all(isinstance(comment, str) for comment in comments):
            raise TypeError("comments must be a list of strings")
        instance = super().__new__(cls)
        instance.value = value
        instance.comments = comments
        return instance

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_output__LineWithComments___new___2_test_invalid_input
isort/Test4DT_tests/test_isort_output__LineWithComments___new___2_test_invalid_input.py:5:28: E0602: Undefined variable 'Any' (undefined-variable)


"""