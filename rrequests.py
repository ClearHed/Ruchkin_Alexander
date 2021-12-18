import requests
from abc import ABC,abstractmethod

Auth_token = "Bearer TN2tHazNEvAAAAAAAAAAATQ_YJ-coyzwXub5DbFnkeo3Wf-nBquyFw-Va0--DUe_"

class RequestBuilder(ABC):

    @abstractmethod
    def set_body(self, body):
        pass

    @abstractmethod
    def add_header(self, key, value):
        pass

    @abstractmethod
    def set_auth(self):
        pass

    @abstractmethod
    def send_request(self, url):
        pass

class UploadFile(RequestBuilder):
    headers = {}
    body = {}

    def set_body(self, data):
        self.body = data

    def add_header(self, key, value):
        self.headers[key] = value

    def set_auth(self):
        self.headers['Authorization'] = Auth_token

    def send_request(self, url):

        return requests.post(url=url, headers=self.headers, data=self.body)

class GetData(RequestBuilder):
    headers = {}
    body = {}

    def set_body(self, file_path):
        self.body = {"file": file_path}

    def add_header(self, key, value):
        self.headers[key] = value

    def set_auth(self):
        self.headers['Authorization'] = Auth_token

    def send_request(self, url):
        return requests.post(url=url, headers=self.headers, json=self.body)


class DeleteFile(RequestBuilder):
    headers = {}
    body = {}

    def set_body(self, file_path):
        self.body = {"path": file_path}

    def add_header(self, key, value):
        self.headers[key] = value

    def set_auth(self):
        self.headers['Authorization'] = Auth_token

    def send_request(self, url):

        return requests.post(url=url, headers=self.headers, json=self.body)