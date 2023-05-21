import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweets_with_hashtag(hashtag, num_tweets, start_date = '2023-05-12', end_date = '2023-05-18'):
    tweets = []
    query = f'#{hashtag} since:{start_date} until:{end_date}'

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets.append(tweet)

        if i + 1 >= num_tweets:
            break

    return tweets

def convert_tweets_to_dataframe(tweets):
    tweet_list = []

    for tweet in tweets:
        tweet_list.append({
            'ID': tweet.id,
            'Date': tweet.date,
            'Content': tweet.content,
            'Username': tweet.user.username,
            'Retweets': tweet.retweetCount,
            'Likes': tweet.likeCount,
            'Replies': tweet.replyCount,
            'Quote Tweets': tweet.quoteCount,
            'Hashtags': tweet.hashtags,
        })

    return pd.DataFrame(tweet_list)

# Example usage
hashtag = 'hildabaci'
num_tweets = 10000

tweets = scrape_tweets_with_hashtag(hashtag, num_tweets)
df = convert_tweets_to_dataframe(tweets)

print(df.head())
print(df.shape)

df.to_csv('data/hilda_baci_data.csv', index = False)