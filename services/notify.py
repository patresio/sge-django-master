import requests


class Notify:
    def __init__(self):
        self.__base_url = "http://127.0.0.1:8001"

    def send_order_event(self, data):
        requests.post(
            url=f"{self.__base_url}/api/v1/webhooks/order/",
            json=data,
        )
