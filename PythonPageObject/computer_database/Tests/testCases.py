# -*- coding: utf8 -*-
# we should add test cases here because we can miss some cases while writing automation code or

# for maintainability, we can separate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]

testCases = [
    # [severity, description]
    ['Regression', 'When user goes to main homepage, page should be loaded and return a 200 status code'],
    ['Regression', 'The user is able to add a computer entry via Homepage'],
    ['Regression', 'The user searches for a computer using the filter text field'],
]