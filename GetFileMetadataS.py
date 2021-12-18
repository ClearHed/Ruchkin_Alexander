from __future__ import annotations
from behave import *
from rrequests import GetData
import sys
import pathlib
sys.path.insert(1, pathlib.Path(__file__).parent.parent.resolve())



class GetFMS():
    def __init__(self):
        self.Builder = GetData()
        self.response = ''

    @given(u'uploaded file')
    def path(self):
        self.Builder.set_body("/WebAPIi/Problem.png")
        self.Builder.add_header("Content-Type", "application/json")
    
    @when(u'I send POST request to DropBox https://api.dropboxapi.com/2/sharing/get_file_metadata')   
    def post_request(self):
        self.response = self.Builder.send_request('https://api.dropboxapi.com/2/sharing/get_file_metadata')
    
    @then(u'I get response "200 OK"')
    def response_validation(self):
        if "<Response [200]>" == str(self.response):
            return False
        else:
            return True