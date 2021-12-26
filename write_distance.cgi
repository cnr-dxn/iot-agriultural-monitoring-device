#!/usr/bin/python3

import urllib.parse
from urllib.parse import urlparse
from urllib.parse import parse_qs
import sys
import os
import mariadb
#import cgitb
import cgi
import requests
import time

# function to print the headers of the html
def headers():
	print("Content-type: text/html")
	print('')

if __name__ == "__main__":
	#cgitb.enable() # enable error printing
	headers() # add the headers to the HTML

	connection = mariadb.connect( # create a connection to the locally hosted MySQL database
		user="###",
		password="########",
		host="127.0.0.1",
		port=3306,
		database="distance_data" # use the proper database
	)
	
	currentCursor = connection.cursor() # create a cursor to enable editing of the database

	url = os.environ["REQUEST_URI"] # obtain the url calling the CGI script 
	parsed = urlparse(url) # parse it to locate the values of the 'event' and 'data' variables

	flag = parse_qs(parsed.query)['event'][0] # obtain the event
	fetched_data = int(parse_qs(parsed.query)['data'][0]) # obtain the data to insert
	core_id = int(parse_qs(parsed.query)['coreid'][0]) # obtain the device id
	currTime = int(time.time()) # obtain the current time (in epoch time)

	if flag == 'write_distance' and fetched_data is not None: # if the flag calls for writing the distance, 
								  # insert the passed variable into the database
		try:
			currentCursor.execute("INSERT INTO level_data (distance, timestamp, hardware_id) VALUES ({}, {}, {})".format(fetched_data, currTime, core_id))
			print('SUCCESS 200')
		except:
			print('ERROR 400')
	else:
		print('ERROR 600')

	connection.commit() # write all of the changes to the database
	connection.close() # close the connection to the database



