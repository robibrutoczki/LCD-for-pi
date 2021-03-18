#! /usr/bin/env python
import drivers
import requests
import json
from time import sleep

display = drivers.Lcd()
def getBitcoinPrice():
    URL = "https://www.bitstamp.net/api/ticker/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def getEtherPrice():
    URL = "https://www.bitstamp.net/api/v2/ticker/ethgbp/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print (str(getBitcoinPrice())+ "/BTC")
        print (str(getEtherPrice())+"/ETH")
        #BTC
        display.lcd_display_string("Bitcoin last:",1)
        display.lcd_display_string(str(getBitcoinPrice())+ "/BTC",2)
        sleep(2)  # Write line of text to second line of display
        display.lcd_clear()
        
        #ETH
        display.lcd_display_string("Ether last:",1)
        display.lcd_display_string(str(getEtherPrice())+"/ETH",2)
        sleep(2)  # Write line of text to second line of display
                                                                                   
        display.lcd_clear()                                # Clear the display of any data
                                                  # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()



