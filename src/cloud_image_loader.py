import os
from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def add_file(self, json_body):
        number = self._get_progressive_number()
        testfile = os.path.join(os.path.dirname(__file__), 'temp', str(number) + '.json')
        print(testfile)
        f = open(testfile, "w")
        f.write(json_body)
        f.close()
        result = self.pc.uploadfile(files=[testfile])
        os.remove(testfile)
        return result

    def _get_progressive_number(self):
        return 0
