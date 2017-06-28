#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
import argparse
#import thread


relaiAlias = 'Pumpe'


class args(object):
    pass

class Relay:
    pin = 0
    delay = 0
    duration = 0
    showCountdown = False
    
    #Vereinfachte Funktion zum Aktivieren des Relais
    def activate(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
    
    #Vereinfachte Funktion zum Deaktivieren des Relais
    def deactivate(self):
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()
    
    #Hauptfunktion: Mithilfe der gegebenen Argumente wird das Relai gesteuert
    def startCountdown(self):
        if not self.duration > 0:                                                                           #Warnmeldung, wenn DURATION gleich 0 ist: Keine Aktivierung des Relais notwendig, Ende des Skripts
            print 'Die DURATION muss laenger als 0 Sekunden sein [-t DURATION]' 
            return  
                
        if self.delay > 0:                                                                                  #Starten der Startverzoegerung, wenn zugehoeriger Parameter groesser als 0
            print relaiAlias + ' wird in ' + str(self.delay) + ' Sekunden akiviert'     
            for t in range(self.delay):                                                                     #for-Schleife zum Herunterzaehlen
                if self.showCountdown:                                                                      #Countdown wird angezeigt, wenn zugehoeriger Parameter gleich True ist
                    print 'Aktivierung in ' + str(self.delay - t) + ' Sekunden' 
                time.sleep(1)   
                    
        self.activate()                                                                                     #Aktivierung des Relais
        print relaiAlias + ' wurde aktiviert und wird in ' + str(self.duration) + ' Sekunden deaktiviert'
        for t in range(self.duration):                                                                      #for-Schleife zum Herunterzaehlen
            if self.showCountdown:                                                                          #Countdown wird angezeigt, wenn zugehoeriger Parameter gleich True ist
                print 'Deaktivierung in ' + str(self.duration - t) + ' Sekunden'    
            time.sleep(1)   
        print relaiAlias + ' deaktiviert'   
        self.deactivate()                                                                                   #Deaktivierung des Relais
    
def setupArguments():

    #Initialisierung der optionalen Argumente
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-d', action='store', dest='delay', type=int, default=0, help='Verzoegerung beim Start in Sekunden')
    parser.add_argument('-t', action='store', dest='duration', type=int, default=5, help='Dauer in Sekunden, die das Relai aktiviert bleibt (default=5)')
    parser.add_argument('-p', action='store', dest='pin', type=int, default=40, help='Verbindung zum PIN (deafult=40)')
    parser.add_argument('--show-countdown', action='store_true', default=False, help='Akvitivert den Live-Countdown')

    parser.parse_args(namespace=args)

    
if __name__ == '__main__':
    setupArguments()
    
    rel = Relay()
    
    rel.delay = args.delay
    rel.duration = args.duration
    rel.pin = args.pin
    rel.showCountdown = args.show_countdown
    
    rel.startCountdown()
