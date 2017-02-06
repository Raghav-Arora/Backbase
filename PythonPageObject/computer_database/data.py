
# Store Test Data

data = [
    {"name": "Added A1 Computers", "intro_date": "2016-01-01", "discontinued": "2017-02-01"},
]


def get_data(name):
	try:
		return (user for user in data if data["name"] == name).next()
	except:
		print "\n     %s is not defined, enter a valid name.\n" %name
