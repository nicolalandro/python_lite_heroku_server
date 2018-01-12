import json
import os
from pcloud import PyCloud


def loadCredentialFromFilePath():
    uname = os.environ['pcloud_uname']
    password = os.environ['pcloud_password']
    return uname, password


class CloudImageLoader(object):
    def __init__(self):
        uname, password = loadCredentialFromFilePath()
        self.pc = PyCloud(uname, password)

    def add_file(self, json_body):
        number = self._get_progressive_number()
        testfile = os.path.join(os.path.dirname(__file__), 'file_to_upload', str(number) + '.json')
        print(testfile)
        f = open(testfile, "w+")
        f.write(json_body)
        f.close()
        result = self.pc.uploadfile(files=[testfile])
        os.remove(testfile)
        return result

    def get_dataset_list(self):
        lis = self._list_remote_folder()
        return lis['metadata']['contents']

    def _get_progressive_number(self):
        try:
            lis = self._list_remote_folder()
            numer_str = lis['metadata']['contents'][-1]['name'].replace('.json', '')
            integer_progressive_number = int(numer_str) + 1
            print(integer_progressive_number)
            return integer_progressive_number
        except:
            return 0

    def _list_remote_folder(self):
        json_list = str(self.pc.listfolder(folderid=0)).replace("'", '"')
        json_list = json_list.replace("False", '"False"').replace("True", '"True"')
        lis = json.loads(json_list)
        return lis
