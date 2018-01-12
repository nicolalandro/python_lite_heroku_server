#!/usr/bin/python
import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/src/file_to_upload/pcloud.credential', 'w') as pcloudfile:
    pcloudfile.write(os.environ['pcloud_uname'] + "," + os.environ['pcloud_password'])
