from gpiozero import CPUTemperature
import os
import time


class RobotCPU:
    def GetTemp(self):
        return CPUTemperature().temperature

    def Reboot(self):
        os.system('sudo reboot now')

    def run(self):
        while True:
            time.sleep(5)
            print("Current Temp: ", GetTemp())
            if GetTemp() > 45:
                print("Warning : Over Temparature Rebooting ...")
                Reboot()
