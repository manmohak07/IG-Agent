
# AI Comment Bots for Instagram and X (Twitter)

Hey folks! I've whipped up this fun little project: AI agents that dive into Instagram and X (formerly Twitter) to leave cryptic, philosophical comments on posts. Imagine Kafka and Dostoevsky teaming up in the digital age. That's the vibe. The bots pull recent posts based on random hashtags related to these literary giants, generate short, enigmatic responses using Google's Gemini AI, and post them as comments or replies.

I've got two agents here: one for Instagram and one for X. They're similar in spirit but tailored to each platform's quirks.

## What Makes This Cool?

-   **Philosophical Flair**: Comments are short, mysterious, and inspired by Kafka and Dostoevsky – perfect for literary or existential posts.
-   **Random Hashtags**: Picks from a list like #kafka, #dostoevsky, #themetamorphosis to keep things fresh.
-   **AI-Powered**: Uses Google's Gemini to craft responses that feel deep and cryptic.
-   **Safe and Slow**: Built-in delays to avoid spamming and getting flagged by the platforms.

Just a heads up: I've created a Twitter (X) agent too, but it won't work if you're on the free tier of an X developer account. The free tier is mostly read-only – you'll need at least the Basic tier (which is paid) to post replies. Check X's developer docs for the latest on that.

## Prerequisites

-   Python 3.8 or higher (because who wants old bugs?).
-   Accounts on Instagram and X (with developer access for X).
-   A Google Gemini API key (grab one from Google AI Studio).
-   A `.env` file in the project root with your secrets:
    
    ```
    # For Instagram
    IG_USERNAME=your_insta_username
    IG_PASS=your_insta_password
    
    # For X (Twitter)
    X_API_KEY=your_x_api_key
    X_API_SECRET=your_x_api_secret
    X_ACCESS_TOKEN=your_x_access_token
    X_ACCESS_TOKEN_SECRET=your_x_access_token_secret
    
    # Shared
    API_KEY=your_gemini_api_key
    
    ```
    

## Installation

Follow these steps

1.  Clone the repo:
    
    ```bash
    git clone https://github.com/manmohak07/IG-Agent.git    
    ```
    
2.  Set up a virtual environment (highly recommended to keep things tidy):
    
    ```bash
    python -m venv venv
    source venv/bin/activate 
    
    ```
    
3.  Install the dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4.  Fill in your `.env` file with the creds mentioned above.
    

## Usage

Fire up the bots separately. They're in different scripts.

### Instagram Bot

-   Run: `python ig_agent.py`
-   What happens:
    -   Logs into Instagram.
    -   Grabs a random hashtag like #kafkaesque.
    -   Fetches the 3 latest posts.
    -   Generates and posts a philosophical comment on each.
    -   Pauses 5 seconds between posts to play nice.

### X (Twitter) Bot

-   Run: `python twt_agent.py`.
-   What happens:
    -   Authenticates with X.
    -   Picks a random hashtag.
    -   Searches for 3 recent English tweets (no retweets).
    -   Crafts a short comment (under 100 chars) and replies to each tweet.
    -   Waits 5 seconds between replies.

**Remember, for X: If you're on the free dev tier, searching might work, but posting replies won't. Upgrade to Basic or higher for full functionality.**

## Project Structure

-   `ig_agent.py`: The main script for the Instagram bot.
-   `twt_agent.py`: The main script for the X (Twitter) bot.
-   `utils/hashtag_gen.py`: Shared utility to pick random literary hashtags.
-   `.env`: Your secret sauce (gitignore'd, of course).
-   `requirements.txt`: All the Python libs you'll need.

## Dependencies

Peek at `requirements.txt` for the details, but highlights include `instagrapi` for Insta, `tweepy` for X, `google-generativeai` for the brainy bits, and `python-dotenv` for env handling.

## A Few Tips and Caveats

-   **Rate Limits**: The 5-second sleep is there to keep your account safe. Tweak if you dare, but don't blame me if you get temporarily locked out!
-   **Instagram Login**: If you have 2FA on, `instagrapi` might hiccup. Consider disabling it for bot use (or use a dedicated account).
-   **Gemini Model**: The scripts use models like 'gemini-1.5-flash' or similar – feel free to experiment with others if you have access.
-   **Error Handling**: I've added some basic try-excepts, but always check the console for issues.
-   **Ethical Note**: Bots are fun, but use responsibly. Follow platform rules, and don't spam. This is for educational vibes only.

If you run into snags or have ideas to improve, hit me up in the issues!

## Disclaimer

This is a hobby project. I'm not liable if your accounts get grumpy with the platforms. Always respect TOS :)
