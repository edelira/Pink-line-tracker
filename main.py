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



	trainList = ['54th/Cermak','Kostner','Pulaski','Central Park','Western',
	             'Damen','18th','Polk','Ashland','Morgan','Clinton','Clark/Lake',
	             'State/Lake','Randolph/Wabash','Adams/Wabash','Harold Washington Library-State/Van Buren,',
	             'LaSalle/Van Buren','Washington/Wells','Cicero','Kedzie','California']

	for i in trainList:
	    if i in trains:
	        print i

