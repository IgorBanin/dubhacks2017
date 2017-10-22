import praw
import time
import os

example_list = []

def bot_login():
    print("Logging in...")
    reddit = praw.Reddit(client_id ='ndZcPVKzPUPeuQ',
                     client_secret ='zRsrBHcE2lU3W529wc5J0GCekg0',
                     username='testbot2233',
                     password='snoo123',
                     user_agent='URL shortener')
    print("Login finished.")
    return reddit

def run_bot(reddit):

    for comment in reddit.subreddit('test').stream.comments():
        try:
            if "https" in comment.body:
                s = comment.body
            
                print(comment.body)
                words = comment.body.split()
                for word in words:
                    if "https" in word:
                        print(word)
                        url = word
                print("URL with \"https\" found!")
                comment.reply("This link saves [lives!](" + url + ")")

##                              \n" + \
##                              "To learn more visit [here]()")
                time.sleep(3600)

        except praw.exceptions.PRAWException as e:
            pass
        
    print("Sleeping for 10 seconds")



reddit = bot_login()

while True:
    run_bot(reddit)





##subreddit = reddit.subreddit('all')



##hot_python = subreddit.hot(limit = 5)
##
##for submission in hot_python:
##    if not submission.stickied:
##        
##        submission.comments.replace_more(limit=0)
##        
##        for comment in submission.comments.list():
##            print(20*'-')
##            print('Parent ID:', comment.parent())
##            print('Comment ID:', comment.id)
##            print(comment.body)

##
##for comment in subreddit.stream.comments():
##    try:
##        parent_id = str(comment.parent())
##        original = reddit.comment(parent_id)
##        print('Parent:')
##        print(original.body)
##       print('Reply:')
##        print(comment.body)
##    except praw.exceptions.PRAWException as e:
##        pass
    

                    
            
        


