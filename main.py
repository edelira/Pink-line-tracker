import time
from xml.dom import minidom
import urllib
import inflect # Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words

API_key = "Place your API key here"

while True:
	url_str = ('http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=%s&rt=pink') %API_key
	xml_str = urllib.urlopen(url_str).read()
	xmldoc = minidom.parseString(xml_str)

	nextStaNm = xmldoc.getElementsByTagName('nextStaNm') #

	current_trains = []
	j = 0 #with multiple nextStaNm values, we need to go through the XML for multiple values. J will be used soon.
	p = inflect.engine() #this is used to convert numbers to words
	for train in range(10): #for loop to go through loop 10 times
		try: #using try because the number of trains available at once changes. program would crash when looking for a value that doesn't exist.
			train = nextStaNm[j].firstChild.nodeValue # allows code to scan through XML and parse each section containing 'nextStaNm'
			j += 1 # add one to each loop to continue parsing XML
			print (p.ordinal(j) + " train is at " + train)
			current_trains.append(train)
		except IndexError: #used for error handling preventing program from crashing when program tries to find a train number that doesn't exists
			train = 'null'
			print train
	# prints all nextStaNm in the XML doc

	print  ', '.join(current_trains)
	time.sleep(5) # pause added to refresh program every 5 seconds to prevent request from hitting request cap.

''' CODE BELOW IS INCOMPLETE AND WILL BE USED WHEN WIRING LED STRIP TO Pi


	trainList = ['54th/Cermak','Kostner','Pulaski','Central Park','Western',
	             'Damen','18th','Polk','Ashland','Morgan','Clinton','Clark/Lake',
	             'State/Lake','Randolph/Wabash','Adams/Wabash','Harold Washington Library-State/Van Buren,',
	             'LaSalle/Van Buren','Washington/Wells','Cicero','Kedzie','California']

	for i in trainList:
	    if i in trains:
	        print i
'''


