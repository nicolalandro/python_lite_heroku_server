import os
from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def list_folder(self):
        testfile = os.path.join('/home/mint', 'Scrivania', 'test.txt')
        f = open(testfile, "w")
        f.write("test")
        f.close()
        self.pc.uploadfile(files=[testfile])
        return self.pc.listfolder(folderid=0)
