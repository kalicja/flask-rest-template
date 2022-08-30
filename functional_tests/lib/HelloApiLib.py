import app_rest_client
from assertpy import assert_that

class HelloApiLib:

    def __init__(self):
        self.app_client=None
        self.response = None

    def service_is_running_on(self, url):
        self.app_client = app_rest_client.AppRestClient(url)

    def there_was_no_posted_hellos(self):
        response = self.app_client.clear_data()
        assert_that(response).is_equal_to(200)

    def requesting_all_hello(self):
        self.response = self.app_client.get_all_hellos()

    def add_hello(self, greeting, sender):
        self.app_client.add_hello(greeting, sender)

    def get_hello_with_id(self, id):
        self.response=self.app_client.get_hello(id)

    def result_is_empty_list(self):
        assert_that(self.response).is_equal_to([])

    def result_is(self, greeting, sender):
        assert_that(self.response).is_equal_to({'greeting':greeting, 'sender':sender})