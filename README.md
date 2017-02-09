# Backbase

Backbase Assignment

The directory contains the Test Script with the tests that cover the CRUD operation of the Application under Test.
The code is written in Python and is using the Page Object Model to navigate around the website.

The automated tests are indicated within the spreadsheet under the Automated column with a 'Y'. In the next column are the name of the tests to cross reference against testCases.py

The first tab within the spreadsheet contains some brief notes and stats.
There is a third hidden tab ('Data') but it just contains the values (Pass/Fail/Not Tested)


Edit: Tests submitted run on the UI Level, however could be improved (more stable) by using the following code for adding computers/editing the computer entry. Will not get the success message so assertion would have to be on the presence of the text within the table.

```python
import requests

def add_computer_non_UI_Level():
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'company':'5','discontinued':'','introduced':'2017-01-01','name':'Computer added using requests Library - More stable than testing on the UI level'}

    session = requests.Session()
    return session.post('http://computer-database.herokuapp.com/computers/new',headers=headers,data=payload)
```
