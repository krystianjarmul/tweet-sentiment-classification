## Tweet sentiment classification in Python using Spacy and Scikit-learn


### Requirements 
* Docker

### Installation
Download source code
```
git clone https://github.com/krystianjarmul/tweet-sentiment-classification.git
```
Go to project directory
```
cd tweet-sentiment-classification
```
Build and run docker container
```
docker build -t tweet_classifier . && docker run -it -p 5000:5000 tweet_classifier
```

### Usage
Go to 127.0.0.1:5000 and create POST request using '/classify' endpoint with 'text': str parameter, e.g.
```
curl -X POST 127.0.0.1:5000/classify -H "Content-Type: application/json" -d "{\"text\":\"I love Python.\"}"
# {
#   "sentiment": "positive",
#   "text": "I love Python."
# }
```
