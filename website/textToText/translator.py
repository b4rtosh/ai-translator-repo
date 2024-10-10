import os

import requests, uuid
from dotenv import load_dotenv


def translateToFrom(langFrom, langTo, text):
    # Add your key and endpoint
    load_dotenv()
    key = os.getenv('API_KEY')
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "westeurope"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': langFrom,
        'to': langTo
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multiservice or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    if request.status_code != 200:
        raise Exception(request.status_code, request.text)
    return request.json()[0]['translations'][0]['text']
