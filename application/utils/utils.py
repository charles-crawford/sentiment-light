from flair.models import TextClassifier
from flair.tokenization import Sentence


def load_model():
    return TextClassifier.load('en-sentiment')


sentiment_model = load_model()


def get_sentiment(text):
    sentence = Sentence(text)
    sentiment_model.predict(sentence)
    sentence = sentence.to_dict()
    del sentence['entities']
    return sentence
