# Cellular IoT Agriultural Monitoring Device

A contract for Dixon & Hau, LLC involving the development of a cellular IoT device that tracks irrigation water levels via utilization of an ultrasonic sensor wired to a Particle Photon, which recorded and uploaded measurement data to a cloud-hosted SQL database via Python CGI scripts hosted on a Linode server.

**Cellular IoT Device**: This device utilizes a cellular-IoT-based component that allows for completely autonomous interaction with the cloud-hosted SQL database anywhere where the device in question has reliable cellular reception.

**Tracks Water Levels via Ultrasonic Sensor**: To accurately measure the levels of the irrigation, the cellular-enabled Particle Photon was wired to an ultrasonic sensor, which recorded the height at preset time intervals and reported these levels to the server. 

**Utilization of REST APIs to Upload Data**: To upload the data, the Photon utilized a REST API built in to the Linode Server’s architecture to transfer the measurement data. The REST API would transfer this data to a Cloud-hosted SQL database, which stored data such as the height, the model number, and the time measurement was taken.

## File Structure

The code included is housed in the HTML folder of the Linode server's web server directory to enable the CGI scripts. The main CGI script that utilizes a REST API to log the data is:
```
write_distance.cgi
```
The secondary CGI script that logs general data regarding each log within the main database (largely for debugging purposes) is:
```
write_general.cgi
```
*NOTE: For privacy purposes, the login information for the database had to be redacted. However, the REST APIs are still functional, and can be called manually with the following url:
```
http://198.58.97.240/reidtest/write_distance.cgi?event=write_distance&data=169&published_at=2021-12-22T20%3A12%3A02.212Z&coreid=250020001847343438323536
```
Where data is the height (in cm) that the sensor records, and the event in question is write_distance


**alteredScraper.py** updates the database with new titles found at that time

**combined.py** provides a test to examine the results of the framework's update (by providing a simple interface for the user to use)

