#include "HC_SR04.h"

int i;
double cm = 0.0;
double minCm = 5;
double maxCm = 200;

int trigPin = D4;
int echoPin = D5;
HC_SR04 rangefinder = HC_SR04(trigPin, echoPin, minCm, maxCm);

void setup() {
    	Serial.begin(9600);
	pinMode( D7, OUTPUT);
	digitalWrite( D7, LOW );
}

void loop() {
    	cm = rangefinder.getDistanceCM();
	Serial.println( cm );
        bool success =  Particle.publish("write_distance", String::format("%d", int(cm) ) );

	if ( success && cm > 0) {
		// flash LED; number of flashes correlates to distance
		for ( int i = 0; i < int( cm/4) ; i++ ) {
			digitalWrite( D7, HIGH ); delay(30); digitalWrite( D7, LOW ); delay(30);
		}
	} else {
		// one long flash for failure
		digitalWrite( D7, HIGH ); delay(2000); digitalWrite( D7, LOW ); 
	}

	delay(30000); // every 30 secs
}

