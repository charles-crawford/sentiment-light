from flask import json, Response
from flask_restx import Resource, Namespace

api = Namespace("healthcheck", description="Health Check")


@api.route('/', methods=['GET'])
class HealthCheck(Resource):

    @api.response(200, 'OK')
    def get(self):
        return Response(json.dumps({'healthcheck': 'OK'}), 200, headers={'Content-Type': 'application/json'})
