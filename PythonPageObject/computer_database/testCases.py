# Test case objectives are defined here
# For easy maintainability, the testCases could be split into separate arrays.(Create, Read, Update, Delete).
# For this assignment, the test case objectives were put in one array.

def test_cases(number):
    return testCases[number]

testCases = [
    # [severity, description]
    ['Regression', 'When user goes to main homepage, page should be loaded and return a 200 status code'],
    ['Regression', 'The user is able to add a computer entry via Homepage'],
    ['Regression', 'The user is able to add a computer entry via Homepage via direct link'],
    ['Regression', 'The user inputs invalid computer names to attempt to break the website'],
    ['Regression', 'The user searches for a computer using the filter text field'],
    ['Regression', 'The user searches for a computer using the filter text field via direct link'],
    ['Regression', 'The user edits a computer entry'],
    ['Regression', 'The user edits a computer entry via direct link'],
    ['Regression', 'The user edits a computer entry via direct link for a computer not in the table'],
    ['Regression', 'The user deletes the computer details'],
    ['Regression', 'The user deletes the computer details via direct link'],
]