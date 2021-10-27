# sample request for the single prediction
curl --location --request POST 'http://0.0.0.0:5001/sentiment/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"plain_text": "Some text that could be good or bad."}'

# response: {"labels": [{"confidence": 0.9921161532402039, "value": "NEGATIVE"}], "text": "Some text that could be good or bad."}

# sample request for the single prediction from your local machine
# be sure to use your EC2's IP address
#curl --location --request POST 'http://{your-ec2-ip}:5001/sentiment/predict' \
#--header 'Content-Type: application/json' \
#--data-raw '{"plain_text": "Some text that could be good or bad."}'