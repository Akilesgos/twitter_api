import twitter

CONSUMER_KEY = 'RlWimW7fHRHo7B8dZKvylgRue'
CONSUMER_SECRET = 'CvhAiepsRMesovmNcPiOYHEC1OprbsSucHuhbraZ6f3amJhHyn'
ACCESS_TOKEN = '968148342814531584-oSvveXcLM5UaukjoTS9KDaC7vN314Hf'
ACCESS_TOKEN_SECRET = 'Zziut5CYCmOIOvt4DW65EbRFwDROCS2ldJPX4Xdg0wdae'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

print(api.VerifyCredentials())

follwers = api.GetFollowers()
friends = api.GetFriends()
status_var = 'Hi, i love shiba-inu'
update_status = api.PostUpdates(status=status_var)

new_messsage = api.PostDirectMessage(screen_name='justinmitchel',
                                     text='Hi there')
print(new_messsage)

new_magic_message = api.PostDirectMessage(screen_name='MagicJohnson',
                                          text='Hey Magic! Big fan.')
print(new_magic_message)

length_status = twitter.twitter_utils.calc_expected_status_length(
    status=status_var)

api.PostDirectMessage(user, text)  # sent messege


'''
>>> api.GetUser(user)
>>> api.GetReplies()
>>> api.GetUserTimeline(user)
>>> api.GetHomeTimeline()
>>> api.GetStatus(status_id)
>>> def GetStatuses(status_ids)
>>> api.DestroyStatus(status_id)
>>> api.GetFriends(user)
>>> api.GetFollowers()
>>> api.GetFeatured()
>>> api.GetDirectMessages()
>>> api.GetSentDirectMessages()
>>> api.PostDirectMessage(user, text)
>>> api.DestroyDirectMessage(message_id)
>>> api.DestroyFriendship(user)
>>> api.CreateFriendship(user)
>>> api.LookupFriendship(user)
>>> api.VerifyCredentials()
'''
