import praw
import random

reddit = praw.Reddit(client_id='UTZBH866L0rrxDxdaXs8bA',
                     client_secret='nye34KQGLICj4ftmUmiFhcQJKMx3bw',
                     user_agent='<console:Depressed:1.0>',
                     username='Depressed-Reply-Bot',
                     password='depressedreplybot')

subreddit = reddit.subreddit("television")

sad_quotes = ["All our dreams can come true, if we have the courage to pursue them. - Walt Disney",
              "The secret of getting ahead is getting started. - Mark Twain",
              "I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed. - Michael Jordan",
              "Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve. - Mary Kay Ash"]

for submission in subreddit.hot(limit=10):
    #print("***********")
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("-------")
                print(comment.body)
                random_index = random.randint(0, len(sad_quotes) - 1)   #Picking a random number between 0 and however long Sad Quotes is
                comment.reply(sad_quotes[random_index])