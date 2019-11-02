# import libraries
import time
import os
from datetime import datetime


class VisonOnHome:
    def current_time(self):
        now = datetime.now()
        return now.strftime("%d-%m-%y-%H:%M:%S")

    def take_snap(self):
        os.system(
            'fswebcam -r 1280x720 -S 3 --jpeg 100 --save /home/pi/webcam/'+str(self.current_time())+'.jpg')
        time.sleep(5)

    def take_shot(self, lenght=10):
        # take video
        os.system(
            'ffmpeg -t '+str(lenght)+' -f v4l2 -framerate 25 -video_size 1280x720 -i /dev/video0 ' + str(self.current_time()) + '.mkv')
        time.sleep(5)

    def upload(self, file_path):
        return file_path
