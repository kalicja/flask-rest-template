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
class HellosApi(Resource):
    '''Show a list of hello item, and add new hello'''
    @api_namespace_hello_world_api.marshal_list_with(hello_moodel)
    def get(self):
        return hello_repo.get_all()

    @api_namespace_hello_world_api.expect(hello_moodel)
    @api_namespace_hello_world_api.marshal_with(hello_moodel, code=201)
    def post(self):
        payload = api_namespace_hello_world_api.payload
        hello = Hello(greeting=payload['greeting'], sender=payload['sender'])
        hello_repo.save(hello)

@api_namespace_hello_world_api.route('/<int:id>', methods=['GET', 'DELETE', 'PUT'])
@api_namespace_hello_world_api.param('id', 'hello identifier')
class HelloApi(Resource):
    '''Show a single hello item, update it and delete'''
    @api_namespace_hello_world_api.marshal_with(hello_moodel)
    def get(self, id):
        '''Fetch given hello'''
        return hello_repo.get(id)

    @api_namespace_hello_world_api.response(204,'Hello deleted')
    def delete(self, id):
        return hello_repo.delete(id)

    @api_namespace_hello_world_api.expect(hello_moodel)
    @api_namespace_hello_world_api.marshal_with(hello_moodel, code=201)
    def put(self, id):
        payload = api_namespace_hello_world_api.payload
        hello = Hello(greeting=payload['greeting'], sender=payload['sender'])
        return hello_repo.update(id, hello)

@api_namespace_hello_world_api.route('/clear-data', methods=['DELETE'])
class TestSupport(Resource):

    def delete(self):
        hello_repo.hellos={}
        hello_repo.last_id=0