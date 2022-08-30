
from flask_restplus import Namespace, Resource, fields

from flask_rest_demo.repository.hello_repo import HelloRepo, Hello

api_namespace_hello_world_api=Namespace('hello-world', description='Hello World demo app')
api_namespace_hello_world_api.model('Hello', {
    'greetings': fields.String(),
    'sender':fields.String()
})
args_parser = api_namespace_hello_world_api.parser()

@api_namespace_hello_world_api.route('/', methods=['GET'])
class HelloApi(Resource):
    def __init__(self):
        self.hello_repo = HelloRepo()

    def get(self):
        return self.hello_repo.get_all()

    def post(self, hello):
        self.create(hello)


