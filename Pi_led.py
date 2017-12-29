import time
from xml.dom import minidom
import urllib
#import inflect # Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words. NOT DEFAULT MODULE ON RASPBERRY PI
from neopixel import *


# LED strip configuration:
LED_COUNT      = 22      # Number of LED pixels.
LED_PIN        = 18       # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
colorWipe(strip, Color(0, 0, 0))


API_key = "Place your API key here"

while True:
	colorWipe(strip, Color(0,0,0))
	url_str = ('http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=%s&rt=pink') %API_key
	xml_str = urllib.urlopen(url_str).read()
	xmldoc = minidom.parseString(xml_str)

	nextStaNm = xmldoc.getElementsByTagName('nextStaNm') #

	current_trains = []
	j = 0 #with multiple nextStaNm values, we need to go through the XML for multiple values. J will be used soon.
	#p = inflect.engine() #this is used to convert numbers to words. NOT DEFAULT MODULE ON PI
	for train in range(10): #for loop to go through loop 10 times
		try: #using try because the number of trains available at once changes. Program would crash when looking for a value that doesn't exist.
			train = nextStaNm[j].firstChild.nodeValue # allows code to scan through XML and parse each section containing 'nextStaNm'
			j += 1 # add one to each loop to continue parsing XML
			#print (p.ordinal(j) + " train is at " + train) inflect package not installed on pi by default. NOT DEFAULT MODULE ON PI
			print train
			current_trains.append(train)
		except IndexError: #used for error handling preventing program from crashing when program tries to find a train number that doesn't exists
			train = 'null'
			#print train

	print  ', '.join(current_trains)

	trainList = ['54th/Cermak','Cicero','Kostner','Pulaski','Central Park','Kedzie','California','Western',
	             'Damen','18th','Polk','Ashland','Morgan','Clinton','Clark/Lake',
	             'State/Lake','Washington/Wabash','Adams/Wabash','Harold Washington Library-State/Van Buren,',
	             'LaSalle/Van Buren','Quincy','Washington/Wells']

	for i in trainList:
	    if i in current_trains:
	        strip.setPixelColor((trainList.index(i)),Color(255,20,147))
            strip.show()

	time.sleep(5) # pause added to refresh program every 5 seconds to prevent request from hitting request cap.



