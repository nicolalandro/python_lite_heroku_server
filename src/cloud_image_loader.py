import json
import os
from pcloud import PyCloud


def loadCredentialFromFilePath(credential_path):
    with open(credential_path, 'r') as credential_file:
        credential_array = credential_file.read().split(',')
    uname = credential_array[0]
    password = credential_array[1]
    return uname, password


class CloudImageLoader(object):
    def __init__(self):
        credential_path = os.path.join(os.path.dirname(__file__), 'file_to_upload', "pcloud.credential")
        uname, password = loadCredentialFromFilePath(credential_path)
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
