from application.utils.factory import create_app
from waitress import serve
import logging

# Set the logging to info to log into log file
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = create_app()

if __name__ == "__main__":
    serve(app, host='0.0.0.0',  port=5000)
