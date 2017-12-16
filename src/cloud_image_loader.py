from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def list_folder(self):
        return self.pc.listfolder(folderid=0)
