# Welcome to my CTA Pink Line Tracker
This is a little project I put together to track the pink line train using a raspberry pi.



## Getting Started

These instructions will get you a copy of the project up and running on your Raspberry Pi and hopefully give you a
foundation to change the tracker from the pink line to other lines.

### Prerequisites

Before getting this program running on your raspberry pi you would need to learn how to wire your LED strip to the Pi and have a CTA Train API
1. Adafruit has a great tutorial to follow to get wired up. [Wiring up your Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)
2. You need to request a API Key from CTA's website [Requesting API Key](http://www.transitchicago.com/developers/traintracker.aspx)
### Installing
1. Move working directory to where you would like the program installed.

        $ cd ~/
        $ git clone https://github.com/edelira/Pink-line-tracker.git

2. Navigate to the directory created

        $ cd Pink-line-tracker

3.  Open Pi_led.py and add your API Key on line 31 "Place your API key here"

        $ sudo nano Pi_led.py
    Save program and exit.
4.  Run program

        $ sudo python Pi_led.py
5. Enjoy!