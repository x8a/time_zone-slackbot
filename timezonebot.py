import os
import time
import re
from slackeventsapi import SlackEventAdapter
from slack_sdk.web import WebClient

from dotenv import load_dotenv

load_dotenv()

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)

# Example responder to bot mentions
@slack_events_adapter.on("app_mention")
def handle_mentions(event_data):
    event = event_data["event"]
    print(event)
    slack_client.chat_postMessage(
        channel=event["channel"],
        text=f"You said:\n>{event['text']}",
    )

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)