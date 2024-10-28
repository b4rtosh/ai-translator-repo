import requests
from django.core.cache import cache
from django.conf import settings

# Constants
AZURE_TRANSLATOR_LANGUAGES_URL = 'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0'
CACHE_TIMEOUT = 60  # 1 minute in seconds


def get_supported_languages():
    cache_key = 'azure_supported_languages'

    # Check if languages are already cached
    cached_languages = cache.get(cache_key)
    if cached_languages:
        return cached_languages

    # If not cached, fetch from Azure API
    try:
        response = requests.get(AZURE_TRANSLATOR_LANGUAGES_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        languages = response.json().get('translation', {})

        simplified_languages = [
            {'code': code, 'name': details['name']}
            for code, details in languages.items()
        ]
        simplified_languages.sort(key=lambda x: x['name'])
        print(simplified_languages)
        # Cache the response for future use
        cache.set(cache_key, simplified_languages, CACHE_TIMEOUT)
        return simplified_languages

    except requests.RequestException as e:
        # Handle any errors
        print(f"Error fetching languages from Azure API: {e}")
        return None