from __future__ import annotations
from behave import *
import sys
import pathlib
from rrequests import UploadFile


sys.path.insert(1, pathlib.Path(__file__).parent.parent.resolve())

class UploadFileSteps():
    def __init__(self):
        self.Builder = UploadFile()
        self.response = ''

    @given(u'I have /Desktop/Problem.png needed to be uploaded to /WebAPIi/Problem.png')
    def have_picture(self):
        with open(str(pathlib.Path(__file__).parent.resolve())+"/Problem.png", 'rb') as picture:
            data = picture.read()
        self.Builder.set_body(data)
        self.Builder.add_header("Dropbox-API-Arg", "{\"path\":\"/WebAPIi/Problem.png\",\"mode\":\"add\"}")
        self.Builder.set_auth()
        self.Builder.add_header("Content-Type", "application/octet-stream")


    @when(u'I send POST request to DropBox https://content.dropboxapi.com/2/files/upload')
    def send_request(self):
        self.response = self.Builder.send_request('https://content.dropboxapi.com/2/files/upload')


    @then(u'I should get response "200 OK"')
    def check_response(self):
        if "<Response [200]>" == str(self.response):
            return 0
        else:
            return 1

  