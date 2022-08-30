import requests

class AppRestClient:

    def __init__(self, url):
        self.url=url

    def get_all_hellos(self):
        url=f'{self.url}/hello'
        return self._execute_get(url)

    def get_hello(self, id):
        url=f'{self.url}/hello/{id}'
        return self._execute_get(url)

    def add_hello(self, greeting, sender):
        url=f'{self.url}/hello'
        return self._execute_post(url, {'greeting':greeting, 'sender':sender})

    def delete_hello(self, id):
        url=f'{self.url}/hello/{id}'
        return self._execute_delete(url)

    def clear_data(self):
        url=f'{self.url}/hello/clear-data'
        return self._execute_delete(url)

    def _execute_get(self, url):
        r = requests.get(url, verify=False)
        print(f'Request: [url:{url}]')
        print(f'Result: [code:{r.status_code}, body:{r.text}]')
        return r.json()

    def _execute_post(self, url, body):
        r = requests.post(url, verify=False, json=body)
        print(f'Request: [url:{url}]')
        print(f'Result: [code:{r.status_code}, body:{r.text}]')
        return r.json()

    def _execute_delete(self, url):
        r = requests.delete(url, verify=False)
        print(f'Request: [url:{url}]')
        print(f'Result: [code:{r.status_code}, body:{r.text}]')
        return r.status_code