from twython import Twython
from wordnik import *
import time

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'a8fd68b2fe2864675c00f00d00105d1104b42016342ee3dd3'
client = swagger.ApiClient(apiKey, apiUrl)

RUN_EVERY_N_SECONDS = 15 # e.g. 60*5 = tweets every five minutes

class WordsApi(object):
    
    def __init__(self, apiClient):
        self.apiClient = apiClient
        
    def reverseDictionary(self, query, **kwargs):
        """Reverse dictionary search
        Args:
            query, str: Search term (required)
            findSenseForWord, str: Restricts words and finds closest sense (optional)
            includeSourceDictionaries, str: Only include these comma-delimited source dictionaries (optional)
            excludeSourceDictionaries, str: Exclude these comma-delimited source dictionaries (optional)
            includePartOfSpeech, str: Only include these comma-delimited parts of speech (optional)
            excludePartOfSpeech, str: Exclude these comma-delimited parts of speech (optional)
            expandTerms, str: Expand terms (optional)
            sortBy, str: Attribute to sort by (optional)
            sortOrder, str: Sort direction (optional)
            minCorpusCount, int: Minimum corpus frequency for terms (optional)
            maxCorpusCount, int: Maximum corpus frequency for terms (optional)
            minLength, int: Minimum word length (optional)
            maxLength, int: Maximum word length (optional)
            includeTags, str: Return a closed set of XML tags in response (optional)
            skip, str: Results to skip (optional)
            limit, int: Maximum number of results to return (optional)
            
        Returns: DefinitionSearchResults
        """

        allParams = ['query', 'findSenseForWord', 'includeSourceDictionaries', 'excludeSourceDictionaries', 'includePartOfSpeech', 'excludePartOfSpeech', 'expandTerms', 'sortBy', 'sortOrder', 'minCorpusCount', 'maxCorpusCount', 'minLength', 'maxLength', 'includeTags', 'skip', 'limit']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method reverseDictionary" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/words.{format}/reverseDictionary'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('query' in params):
            queryParams['query'] = self.apiClient.toPathValue(params['query'])
        if ('findSenseForWord' in params):
            queryParams['findSenseForWord'] = self.apiClient.toPathValue(params['findSenseForWord'])
        if ('includeSourceDictionaries' in params):
            queryParams['includeSourceDictionaries'] = self.apiClient.toPathValue(params['includeSourceDictionaries'])
        if ('excludeSourceDictionaries' in params):
            queryParams['excludeSourceDictionaries'] = self.apiClient.toPathValue(params['excludeSourceDictionaries'])
        if ('includePartOfSpeech' in params):
            queryParams['includePartOfSpeech'] = self.apiClient.toPathValue(params['includePartOfSpeech'])
        if ('excludePartOfSpeech' in params):
            queryParams['excludePartOfSpeech'] = self.apiClient.toPathValue(params['excludePartOfSpeech'])
        if ('minCorpusCount' in params):
            queryParams['minCorpusCount'] = self.apiClient.toPathValue(params['minCorpusCount'])
        if ('maxCorpusCount' in params):
            queryParams['maxCorpusCount'] = self.apiClient.toPathValue(params['maxCorpusCount'])
        if ('minLength' in params):
            queryParams['minLength'] = self.apiClient.toPathValue(params['minLength'])
        if ('maxLength' in params):
            queryParams['maxLength'] = self.apiClient.toPathValue(params['maxLength'])
        if ('expandTerms' in params):
            queryParams['expandTerms'] = self.apiClient.toPathValue(params['expandTerms'])
        if ('includeTags' in params):
            queryParams['includeTags'] = self.apiClient.toPathValue(params['includeTags'])
        if ('sortBy' in params):
            queryParams['sortBy'] = self.apiClient.toPathValue(params['sortBy'])
        if ('sortOrder' in params):
            queryParams['sortOrder'] = self.apiClient.toPathValue(params['sortOrder'])
        if ('skip' in params):
            queryParams['skip'] = self.apiClient.toPathValue(params['skip'])
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DefinitionSearchResults')
        return responseObject
    
    def getRandomWord(self, **kwargs):
        """Returns a single random WordObject
        Args:
            includePartOfSpeech, str: CSV part-of-speech values to include (optional)
            excludePartOfSpeech, str: CSV part-of-speech values to exclude (optional)
            hasDictionaryDef, str: Only return words with dictionary definitions (optional)
            minCorpusCount, int: Minimum corpus frequency for terms (optional)
            maxCorpusCount, int: Maximum corpus frequency for terms (optional)
            minDictionaryCount, int: Minimum dictionary count (optional)
            maxDictionaryCount, int: Maximum dictionary count (optional)
            minLength, int: Minimum word length (optional)
            maxLength, int: Maximum word length (optional)
            
        Returns: WordObject
        """

        allParams = ['includePartOfSpeech', 'excludePartOfSpeech', 'hasDictionaryDef', 'minCorpusCount', 'maxCorpusCount', 'minDictionaryCount', 'maxDictionaryCount', 'minLength', 'maxLength']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getRandomWord" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/words.{format}/randomWord'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('hasDictionaryDef' in params):
            queryParams['hasDictionaryDef'] = self.apiClient.toPathValue(params['hasDictionaryDef'])
        if ('includePartOfSpeech' in params):
            queryParams['includePartOfSpeech'] = self.apiClient.toPathValue(params['includePartOfSpeech'])
        if ('excludePartOfSpeech' in params):
            queryParams['excludePartOfSpeech'] = self.apiClient.toPathValue(params['excludePartOfSpeech'])
        if ('minCorpusCount' in params):
            queryParams['minCorpusCount'] = self.apiClient.toPathValue(params['minCorpusCount'])
        if ('maxCorpusCount' in params):
            queryParams['maxCorpusCount'] = self.apiClient.toPathValue(params['maxCorpusCount'])
        if ('minDictionaryCount' in params):
            queryParams['minDictionaryCount'] = self.apiClient.toPathValue(params['minDictionaryCount'])
        if ('maxDictionaryCount' in params):
            queryParams['maxDictionaryCount'] = self.apiClient.toPathValue(params['maxDictionaryCount'])
        if ('minLength' in params):
            queryParams['minLength'] = self.apiClient.toPathValue(params['minLength'])
        if ('maxLength' in params):
            queryParams['maxLength'] = self.apiClient.toPathValue(params['maxLength'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'WordObject')
        return responseObject

class StringValue:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'word': 'str'

        }

        self.word = None # str

def main():
    wordApi = WordsApi(client)
    
    a = wordApi.getRandomWord(includePartOfSpeech='noun', minLength=3, maxLength=8)
    b = wordApi.getRandomWord(includePartOfSpeech='adjective', minLength=3, maxLength=8)
    c = wordApi.reverseDictionary(query='food', includePartOfSpeech='noun', limit=1)
    message = 'the %s: %s with a hint of %s' % (a.word, b.word, c.results[0].word)
    message.lower()
    twitter.update_status(status=message)
    print("Tweeted: {}".format(message))
    time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
