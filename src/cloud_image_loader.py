import os
from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def add_file(self, json_body):
        number = 0
        testfile = os.path.join(os.path.dirname(__file__), 'temp', str(number) + '.json')
        print(testfile)
        f = open(testfile, "w")
        f.write(json_body)
        f.close()
        return self.pc.uploadfile(files=[testfile])
