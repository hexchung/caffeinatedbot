# app.py

import os
import time
from random import random
from twython import Twython

CONSUMER_KEY = os.environ['zuuTYMPo0AJwnDRnAYbA68WgV']
CONSUMER_SECRET = os.environ['YZkazKYecPn6EMTqxn4gJByyVJOl0YmlP2Yxb66GvCD3pNV14V']
OAUTH_TOKEN = os.environ['814419060590985216-WJbavA1ss3j4lTvFjZQPuyTS3efeBBf']
OAUTH_TOKEN_SECRET = os.environ['17Y9XoqzFtVJtMhxWs86Ci3uwmk2537HpwMsEtB6fXxSV']
TWEET_LENGTH = 140
TWEET_URL_LENGTH = 21

RUN_EVERY_N_SECONDS = 60*15 # e.g. 60*5 = tweets every five minutes

USERS_TO_IGNORE = []
DO_NOT_FAVORITE_USERS_AGAIN = True

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def favorite_tweet(tweet, handle):
    handle.create_favorite(id=tweet['id'])

def random_favoriting(keywords, handle, favorite_probability=0.2):

    for keyword in keywords:
        xs = handle.search(q=keyword)
        ts = [x for x in xs['statuses']]
        if DO_NOT_FAVORITE_USERS_AGAIN:
            ts = [x for x in ts if x['user']['id'] not in USERS_TO_IGNORE]
        if ts:
            if random() < favorite_probability: 
                print 'Favoriting: ' + ts[0]['text']
                favorite_tweet(ts[0], handle)
                if DO_NOT_FAVORITE_USERS_AGAIN:
                    USERS_TO_IGNORE.append(ts[0]['user']['id'])
                return

def get_urls_of_media_in_tweet(tweet):

    if 'entities' not in tweet or 'media' not in tweet['entities']:
        return []
    return [x['media_url'] for x in tweet['entities']['media']]

def get_mentions(handle, include_entities=False):

    return handle.cursor(handle.get_mentions_timeline,
        include_entities=include_entities)

def get_images_in_mentions(handle):

    for tweet in get_mentions(handle, include_entities=True):
        urls = get_urls_of_media_in_tweet(tweet)
        yield urls

def submit_tweet_with_media(message, mediafile, tweet_to_reply=None, handle=None):

    if not handle:
        handle = twitter_handle()
    media_ids = handle.upload_media(media=open(mediafile))
    if tweet_to_reply is None:
        handle.update_status(status=message,
            media_ids=media_ids['media_id'])
    else:
        # must mention user's name for it to be a reply
        message += ' @' + tweet_to_reply['user']['screen_name']
        handle.update_status(status=message,
            in_reply_to_status_id=tweet_to_reply['id'],
            media_ids=media_ids['media_id'])

def submit_tweet(message, tweet_to_reply=None, handle=None):

    if not handle:
        handle = twitter_handle()
    if tweet_to_reply is None:
        handle.update_status(status=message)
    else:
        # must mention user's name for it to be a reply
        message += ' @' + tweet_to_reply['user']['screen_name']
        handle.update_status(status=message,
            in_reply_to_status_id=tweet_to_reply['id'])

def get_message(handle):

    wordsApi = WordsApi.WordsApi(client)
    message = "the " wordsApi.getRandomWord(partOfSpeech='noun') ": " wordsApi.getRandomWord(partofSpeech='adjective') ", with a " wordsApi.getRandomWord(partOfSpeech='adjective') " " wordsApi.getReverseDictionary('food', partOfSpeech='noun', limit=1) "."
    assert len(message) <= TWEET_LENGTH
    return message

def main():
    handle = twitter_handle()
    USERS_TO_IGNORE.extend([x['user']['id'] for x in handle.get_favorites()])
    while True:
        message = get_message(handle)
        print message
        submit_tweet(message, handle)
        # random_favoriting(['apples', 'oranges'], handle)
        time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
