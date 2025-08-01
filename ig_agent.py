from instagrapi import Client
from utils.hashtag_gen import select_random_hashtag
from dotenv import load_dotenv
import google.generativeai as genai
import time
import os

load_dotenv()

# CONFIG
INSTAGRAM_USERNAME = os.getenv("IG_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("IG_PASS")
GEMINI_API_KEY= os.getenv("API_KEY")
HASHTAG = select_random_hashtag()

genai.configure(api_key=GEMINI_API_KEY)

cl = Client()
cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

medias = cl.hashtag_medias_recent(HASHTAG, amount=3)

def generate_comment(caption):
    prompt = f"""
    You are a fusion of Kafka and Dostoevsky. Write a short, 
    cryptic philosophical comment in response to the following post caption:\n\n"{caption}"\n\nComment:"""

    model = genai.GenerativeModel(model_name='gemini-2.5-flash-lite')
    response = model.generate_content(prompt)
    comment = response.text.strip()
    return comment

for media in medias:
    caption = media.caption_text
    print(f"\nPost Caption: {caption}")
    comment = generate_comment(caption)
    print(f"Generated Comment: {comment}")
    cl.media_comment(media.id, comment)

    time.sleep(5)
