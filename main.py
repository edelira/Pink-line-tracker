import time
from xml.dom import minidom
import urllib


API_key = "Place your API key here"

while True:
	url_str = ('http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=%s&rt=pink') %API_key
	xml_str = urllib.urlopen(url_str).read()
	xmldoc = minidom.parseString(xml_str)

	nextStaNm = xmldoc.getElementsByTagName('nextStaNm')

	try:
		train_zero = nextStaNm[0].firstChild.nodeValue
		print train_zero
	except IndexError:
		train_zero = 'null'
		print train_zero
	try:
		train_one = nextStaNm[1].firstChild.nodeValue
		print train_one
	except IndexError:
		train_one = 'null'
	try:
		train_two = nextStaNm[2].firstChild.nodeValue
		print train_two
	except IndexError:
		train_two = 'null'
	try:
		train_three = nextStaNm[3].firstChild.nodeValue
		print train_three
	except IndexError:
		train_three = 'null'
	try:
		train_four = nextStaNm[4].firstChild.nodeValue
		print train_four
	except IndexError:
		train_four = 'null'
	try:
		train_five = nextStaNm[5].firstChild.nodeValue
		print train_five
	except IndexError:
		train_five = 'null'
	try:
		train_six = nextStaNm[6].firstChild.nodeValue
		print train_six
	except IndexError:
		train_six = 'null'
	# prints all base:OBS_VALUE in the XML doc

	print "Active trains below"
	trains = []
	trains.extend((train_zero,train_one,train_two,train_three,train_four,train_five,train_six))
	print  ', '.join(trains)



	if '54th/Cermak' in trains:

		print "54th/Cermak"

	if 'Kostner' in trains:

		print "Kostner"

	if 'Pulaski' in trains:

		print "Pulaski"

	if 'Central Park' in trains:

		print "Central Park"

	if 'Western' in trains:

		print "Western"

	if 'Damen' in trains:

		print "Damen"

	if '18th' in trains:

		print "18th"

	if 'Polk' in trains:

		print "Polk"

	if 'Ashland' in trains:

		print "Ashland"

	if 'Morgan' in trains:

		print "Morgan"

	if 'Clinton' in trains:

		print "Clinton"

	if 'Clark/Lake' in trains:

		print "Clark/Lake"

	if 'State/Lake' in trains:

		print "State/Lake"

	if 'Randolph/Wabash' in trains:

		print "Randolph/Wabash"

	if 'Adams/Wabash' in trains:

		print "Adams/Wabash"

	if 'Harold Washington Library-State/Van Buren' in trains:

		print "Harold Washington Library-State/Van Buren"

	if 'LaSalle/Van Buren' in trains:

		print "LaSalle/Van Buren"

	if 'Washington/Wells' in trains:

		print "Washington/Wells"

	if 'Cicero' in trains:

		print "Cicero"

	if 'Kedzie' in trains:

		print "Kedzie"

	if 'California' in trains:

		print "California"

