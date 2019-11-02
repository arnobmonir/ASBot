import time
import RPi.GPIO as GPIO
import logging
buzzer = 18


class WaterThePlant:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(buzzer, GPIO.OUT)

    def WaterPump(self, status):
        GPIO.output(buzzer, status)

    def logger(self, mssg):
        logging.basicConfig(
            filename='app.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.warning(mssg)

    def run(self):
        print("Welcome to Auto Pump")
        WaterPump(True)
        logger('Pump On for watering the plant')
        print('Water Pump On')
        time.sleep(15)
        WaterPump(False)
        logger('Successfully completed todays task')
        print('Water Pump off')
