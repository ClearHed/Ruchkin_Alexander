from __future__ import annotations
from behave import *
import sys
import pathlib


sys.path.insert(1, pathlib.Path(__file__).parent.parent.resolve())

from rrequests import DeleteFile

class DeleteFileS():
    def __init__(self):
        self.Builder = DeleteFile()
        self.response = ''

    @given(u'/WebAPIi/Problem')
    def set_file_path(self):
        self.Builder.set_body("/Burkov_Lab7/angry-bladerunner.gif")
        self.Builder.add_header("Content-Type", "application/json")


    @when(u'I send POST request to https://api.dropboxapi.com/2/files/delete_v2')
    def send_request(self):
        self.response = self.Builder.send_request('https://api.dropboxapi.com/2/files/delete_v2')


    @then(u'I get response "200 OK"')
    def response(self):
        if "<Response [200]>" == str(self.response):
            return False
        else:
            return True
