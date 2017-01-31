
#
#	Python GPS Tracking Example
#	SparkFun Electronics, A.Weiss
#	Beerware: if you use this and meet me, you must buy me a beer
#	
#	Function:
#	Takes GPS position and altitude data and plots it on a scaled map image of your
#	choice. Altitude can also be displayed in a separate graph. 
#	
#	The program has a console menu that allows you to configure your connection. 
#	The program will run with either a GPS moudle connected or no moudle connected.
#	If a GPS is connected, the position and altitude data is automatically saved
#	to a file called nmea.txt. If no GPS is connected, you must create your own
#	nmea.txt and fill it with GPGGA NMEA sentences. 
#	A map needs to be created and saved as a file called map.png. When you create
#	your map, note the lat and long of the bottom left and top right corner, in decimal 
#	degrees. Then enter this information into the global variables below. This way, 
#	your the border of your map image can be used as the graph mins and maxs.
#	Once you have a map loaded and a GPS connected, you can run the program and select
#	either your position to be displayed on your map, or display altitude on a separate
#	graph. The maps are not updated in realtime, so you must close the map and run 
#	the map command again in order to read new data. 
import sys
from pynmea import nmea
import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil

######Global Variables#####################################################
# you must declare the variables as 'global' in the fxn before using#
ser = 0
lat = 0
long = 0
pos_x = 0
pos_y = 0
alt = 0
i = 0 #x units for altitude measurment

#adjust these values based on your location and map, lat and long are in decimal degrees
TRX = -105.1621          #top right longitude
TRY = 40.0868            #top right latitude
BLX = -105.2898          #bottom left longitude
BLY = 40.001             #bottom left latitude
BAUDRATE = 9600
lat_input = 0            #latitude of home marker
long_input = 0           #longitude of home marker
count = 0
######FUNCTIONS############################################################ 
def position():
    #opens a the saved txt file, parses for lat and long, displays on map
    global lat, long, lat_input, long_input, pos_x, pos_y, altitude
    global BLX, BLY, TRX, TRY,count
    f1 = open('nmea.txt', 'r') #open and read only
    for line in f1:
        if(line[0] == '\0'):
            f1.close()
            break
        elif(line[4] == 'G'): # $GPGGA
            #print line
            gpgga = nmea.GPGGA()
            gpgga.parse(line)
            lats = gpgga.latitude
            longs = gpgga.longitude
            
       
position()
                        		
	






