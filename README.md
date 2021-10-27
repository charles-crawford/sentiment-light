## An App for Sentiment Analysis

This is a one endpoint RESTful API app that uses a built-in model from the Python library Flair to 
predict the sentiment of the submitted text. It is a transformer based model trained on movie and 
product reviews that is located 
[here](https://nlp.informatik.hu-berlin.de/resources/models/sentiment-curated-distilbert/sentiment-en-mix-distillbert.pt).

### Run the App on AWS EC2
1. [ssh into your AWS EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).
2. [Install Docker on your EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)
3. Clone the repo
4. Change directories into the repo
5. To build and run the app use the command

After Step 1 and 2, use these commands to deploy the app:

`git clone git@github.com:charles-crawford/sentiment-light.git`<br>
`cd sentiment-light`<br>
`docker compose up -d`


### Testing the App
#### In your EC2
Go to your AWS EC2 console and copy the public url for your EC2 instance.
There is a curl request in `applications/test-requests.txt` you can use to check 
if the app is up and running. Run these commands from your EC2 shell:

`chmod +x application/test-requests.sh`<br>
`./application/test-requests.sh`

You should get this respsonse:
`{"labels": [{"confidence": 0.9921161532402039, "value": "NEGATIVE"}], "text": "Some text that could be good or bad."}`

### From your local machine
After starting the app, the documentation is located at `http://{your-host-ip}:5001/.`