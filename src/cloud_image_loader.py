import os
from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def list_folder(self):
        testfile = os.path.join(os.path.dirname(__file__), 'temp', 'test.txt')
        print(testfile)
        f = open(testfile, "w")
        f.write("test")
        f.close()
        return self.pc.uploadfile(files=[testfile])
