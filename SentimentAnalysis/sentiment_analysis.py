import requests, json
# Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyse):
# Define a function named sentiment_analyzer that  
# takes a string input (text_to_analyse) 

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
    
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        
        # Prettify the data
        pretty_response = json.dumps(formatted_response, indent=4, sort_keys=True)
        print(pretty_response, '\n\n')

        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
        
    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
