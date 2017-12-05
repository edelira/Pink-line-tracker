import time
from xml.dom import minidom
import urllib


API_key = "Place your API key here"

while True:
	url_str = ('http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=%s&rt=pink') %API_key
	xml_str = urllib.urlopen(url_str).read()
	xmldoc = minidom.parseString(xml_str)

	nextStaNm = xmldoc.getElementsByTagName('nextStaNm')

	train_zero = train_one = train_two = train_three = train_four = train_five = train_six = ""

	train_check = [train_zero,train_one,train_two,train_three,train_four,train_five,train_six]

	j = 0
	for train in train_check:
		try:
			train = nextStaNm[j].firstChild.nodeValue
			j += 1
			print train
			print j
		except IndexError:
			i = 'null'
			print i
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
	time.sleep(5)