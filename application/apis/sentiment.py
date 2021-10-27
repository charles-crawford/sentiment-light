from flask import json, Response, current_app, request
from flask_restx import Resource, Namespace
from application.utils.utils import get_sentiment
from application.utils.data_transfer_objects import DataTransferObjects

api = Namespace("sentiment", description="Sentiment Analysis")
dtos = DataTransferObjects(api)


@api.route('/predict', methods=['POST'])
@api.doc(responses=dtos.general_responses)
class Sentiment(Resource):

    @api.expect(dtos.plain_text)
    @api.response(200, 'OK', dtos.prediction)
    def post(self):
        try:
            request_body = request.get_json(silent=True)
            plain_text = request_body['plain_text']
        except Exception as e:
            msg = f'Bad Request: {e}'
            current_app.logger.exception(msg)
            return Response(json.dumps({'error': msg}), 400,
                            headers={'Content-Type': 'application/json'})

        try:
            predictions = get_sentiment(plain_text)
            return Response(json.dumps(predictions), 200, headers={'Content-Type': 'application/json'})

        except Exception as e:
            msg = f'Exception processing the request {e}'
            current_app.logger.exception(msg)
            return Response(json.dumps({'error': msg}), 500, headers={'Content-Type': 'application/json'})
