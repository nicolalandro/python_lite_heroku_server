import json
import os
from pcloud import PyCloud
from fs import opener


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

    @property
    def get_dataset_list(self):
        lis = self._list_remote_folder()
        filename_list = lis['metadata']['contents']
        complete_file_list = list()

        uname = os.environ['pcloud_uname'].replace('@', '%40')
        password = os.environ['pcloud_password']
        link = 'pcloud://' + uname + ':' + password + '@/'
        with opener.open_fs(link) as openfs:
            i = 0
            for file_data in filename_list:
                file_name = file_data['name']
                file_size = file_data['size']
                print(file_name, " ", file_size)
                file = openfs.openbin("/" + file_name, mode="r")

                json_string = file.read(file_size).decode('utf-8').replace("'", '"')
                json_obj = json.loads(json_string)
                specie = json_obj['specie']
                img = json_obj['img']

                dict = {
                    'name': file_name,
                    'specie': specie,
                    'img': img,
                }
                complete_file_list.append(dict)
                i += 1
        return complete_file_list

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
