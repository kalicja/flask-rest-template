import json

from flask_restplus import Namespace, Resource, fields

from flask_rest_demo.repository.hello_repo import HelloRepo, Hello

api_namespace_hello_world_api=Namespace('hello', description='Hello World demo app')
hello_moodel=api_namespace_hello_world_api.model('Hello', {
    'greeting': fields.String(),
    'sender':fields.String()
})
args_parser = api_namespace_hello_world_api.parser()
hello_repo = HelloRepo()

@api_namespace_hello_world_api.route('/', methods=['GET', 'POST'])
class HelloApi(Resource):

    @api_namespace_hello_world_api.marshal_list_with(hello_moodel)
    def get(self):
        return hello_repo.get_all()

    @api_namespace_hello_world_api.expect(hello_moodel)
    @api_namespace_hello_world_api.marshal_with(hello_moodel, code=201)
    def post(self):
        payload = api_namespace_hello_world_api.payload
        hello = Hello(greeting=payload['greeting'], sender=payload['sender'])
        hello_repo.save(hello)


