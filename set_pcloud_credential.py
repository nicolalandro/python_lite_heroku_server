#!/usr/bin/python
import sys
import os

if len(sys.argv) > 3 | len(sys.argv) < 2:
    print("Error: number of arguments should be two. Try to run 'python set_pcloud_credential uname password' ")
else:
    with open(os.path.dirname(os.path.abspath(__file__)) + '/src/file_to_upload/pcloud.credential', 'w') as pcloudfile:
        pcloudfile.write(sys.argv[1] + "," + sys.argv[2])
