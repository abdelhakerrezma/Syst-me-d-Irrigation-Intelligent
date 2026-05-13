import RPi.GPIO as GPIO
from rpi_lcd import LCD
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ******* Led *******
LEDR= 27
LEDG= 22
GPIO.setup(LEDR, GPIO.OUT)
GPIO.setup(LEDG, GPIO.OUT)

# ***** LCD Display *****
lcd = LCD()

# ***** Soil Sensor *****
Soil_sensor = 4
GPIO.setup(Soil_sensor, GPIO.IN)

# *****Pump *****
pump= 17
GPIO.setup(pump, GPIO.OUT)

lcd.text("* RASPBERRY PI *",1)
lcd.text("*** TRAINING ***",2)
time.sleep(2)
lcd.clear()

lcd.text("-*-  PROJECT -*-",1)
lcd.text("SMART IRRIGATION",2)
time.sleep(2)
lcd.clear()

lcd.text("SMART IRRIGATION",1)
lcd.text("BY  AERO ENETCOM",2)
time.sleep(2)
lcd.clear()


lcd.text("SMART IRRIGATION",1)
lcd.text("-*- WET SAND -*-",2)

while True:
    if (GPIO.input(Soil_sensor) == True):
        print ("Dry Sand")
        lcd.text("SMART IRRIGATION",1)
        lcd.text("-*- DRY SAND -*-",2)
        time.sleep(2)
        lcd.text("-*- WATERING -*-",2)
        GPIO.output(pump, GPIO.HIGH)
        GPIO.output(LEDR, GPIO.HIGH)
        GPIO.output(LEDG, GPIO.LOW)
    else:
        print("Wet Sand")
        lcd.text("SMART IRRIGATION",1)
        lcd.text("-*- WET SAND -*-",2)
        GPIO.output(pump, GPIO.LOW)
        GPIO.output(LEDR, GPIO.LOW)
        GPIO.output(LEDG, GPIO.HIGH)
        
    time.sleep(1)