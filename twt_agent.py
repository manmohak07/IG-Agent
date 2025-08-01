import tweepy
from utils.hashtag_gen import select_random_hashtag
from dotenv import load_dotenv
import google.generativeai as genai
import time
import os

load_dotenv()

# CONFIG
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
GEMINI_API_KEY = os.getenv("API_KEY")
HASHTAG = select_random_hashtag()


if not all([X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, GEMINI_API_KEY]):
    print("Error: Missing environment variables. Check .env file.")
    exit(1)

try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    exit(1)

try:
    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    user = client.get_me().data
    print(f"Authenticated as @{user.username}")
except tweepy.TweepyException as e:
    print(f"Error authenticating with X: {e}")
    exit(1)

try:
    tweets = client.search_recent_tweets(
        query=f"#{HASHTAG} -is:retweet lang:en",
        max_results=3
    ).data or []
except tweepy.TweepyException as e:
    print(f"Error searching tweets for #{HASHTAG}: {e}")
    exit(1)

def generate_comment(text):
    prompt = f"""
    You are a fusion of Kafka and Dostoevsky. Write a short (max 100 characters), 
    cryptic philosophical comment in response to the following tweet:\n\n"{text}"\n\nComment:"""
    
    try:
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')  # Updated model
        response = model.generate_content(prompt)
        comment = response.text.strip()[:100]
        return comment
    except Exception as e:
        print(f"Error generating comment: {e}")
        return "In the abyss, silence speaks."

for tweet in tweets:
    text = tweet.text
    print(f"\nTweet Text: {text}")
    comment = generate_comment(text)
    print(f"Generated Comment: {comment}")
    try:
        client.create_tweet(
            text=comment,
            in_reply_to_tweet_id=tweet.id
        )
        print("Comment posted successfully")
    except tweepy.TweepyException as e:
        print(f"Error posting comment: {e}")
    
    time.sleep(5)