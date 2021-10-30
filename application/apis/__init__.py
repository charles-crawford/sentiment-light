from flask_restx import Api
from application.apis.sentiment import api as sentiment
from application.apis.healthcheck import api as healthcheck


api = Api(
    title='Sentiment Analysis',
    version='1.0',
    description='Sentiment Analysis'
)

api.add_namespace(sentiment, path='/sentiment')
api.add_namespace(healthcheck)
