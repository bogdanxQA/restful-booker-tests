# common/api/client.py
import requests
import allure
from utils.logger import logger

class APIclient():

    def __init__(self, base_url):
        self.base_url = base_url
        self.base_headers = {
             "Content-Type": "application/json",
             "Accept": "application/json"
        }

    def _request(self, method, endpoint, **kwargs):
        url = f'{self.base_url}{endpoint}'
        headers = self.base_headers.copy()
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        kwargs["headers"] = headers

        # Прикрепляем тело запроса в отчёт Allure (если есть)
        if "json" in kwargs:
            allure.attach(str(kwargs["json"]), name="Request JSON", attachment_type=allure.attachment_type.JSON)
        if "data" in kwargs:
            allure.attach(str(kwargs["data"]), name="Request data", attachment_type=allure.attachment_type.TEXT)

        logger.info(f"Запрос: {method} {url}")

        response = requests.request(method, url, **kwargs)

        # Прикрепляем тело ответа в отчёт Allure
        allure.attach(response.text, name="Response body", attachment_type=allure.attachment_type.TEXT)

        logger.info(f"Ответ: {response.status_code} для {method} {url}")
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)