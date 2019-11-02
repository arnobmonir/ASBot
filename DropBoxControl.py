import dropbox
import time


class DropboxHandeler:
    def __init__(self):
        self.dbx = dropbox.Dropbox(
            '1eIBLPoFzhAAAAAAAAAA4PKJyY5_FiwxvFikMxW6kpbFOEFXFF7n6IqgIVyphvYk')

    def upload(self, file_name):
        f = open(file_name, "rb")
        try:
            self.dbx.files_upload(
                f.read(), '/Webcam/' + file_name, mode=dropbox.files.WriteMode.overwrite)
        except:
            print('Internet Problem')
            time.sleep(15)
            print('Retry...')
            self.upload(file_name)

    def CheckQueue(self):
        files = open("job-queue.txt", "r")
        for file in files:
            self.upload(file[:-1])
