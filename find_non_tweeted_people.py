#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
------------------------
author : iiou16
------------------------
'''

import tweepy
import datetime

# set keys
CONSUMER_KEY = 'xxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxx'
ACCESS_SECRET = 'xxxxxxxx'

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# make API instance
api = tweepy.API(auth)

userid = "iiou16_tech"  # my twitter-id

friends_id_list = api.friends_ids(userid)  # Get all the people my account is following
for f_id in friends_id_list:
    # print(api.get_user(f_id).name)
    try:
        tweet = api.user_timeline(f_id, count=1)
    except Exception as e:
        print(e)

    t_time = tweet[0].created_at  # get tweeted time
    now = datetime.datetime.now()
    one_year = 60 * 60 * 24 * 365  # sec * min * hour * day
    if (now - t_time).total_seconds() > one_year:
        print("user : ", tweet[0].user.name)
        print("tweet_time :", t_time.strftime('%Y-%m-%d'))
        # print(tweet[0].text)
        print()
        api.destroy_friendship(f_id)
