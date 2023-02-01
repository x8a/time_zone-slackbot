import os
import time
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv

load_dotenv()

# Every time we need to install the dependencies run: pip3 install -r requirements.txt

# instantiate Slack client
slack_client = WebClient(os.getenv('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
timezonebot_id = None

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

# @app.command("/hello-socket-mode")
# def hello_command(ack, body):
#     user_id = body["user_id"]
#     ack(f"Hi, <@{user_id}>!")

# @app.event("app_mention")
# def event_test(say):
#     say("Hi there, I'm the bot!")

if __name__ == "__main__":
#    SocketModeHandler(app, os.environ["SLACK_BOT_TOKEN"]).start()

# ID of channel you want to post message to
    channel_id = "CAPJNJXJL"

try:
    # Call the conversations.list method using the WebClient
    result = slack_client.chat_postMessage(
        channel=channel_id,
        text="This is coming from our code! :tada:"
        # You could also use a blocks[] array to send richer content
    )
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")
