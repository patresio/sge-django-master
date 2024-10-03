import requests


class Notify:
    def __init__(self):
        self.__base_url = "https://webhook-test.com"

    def send_event(self, data):
        requests.post(
            url=f"{self.__base_url}/9c45f50acbd3ed07b68ea434365bcf9c",
            json=data,
        )
