import os

from apscheduler.schedulers.blocking import BlockingScheduler
from atproto import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bluesky credentials
BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD")

# Create a Bluesky client
client = Client("https://bsky.social")


def main():
    client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)
    client.post("🙂")


# Scheduling the task
scheduler = BlockingScheduler()

scheduleExpression = "0 */3 * * *"  # Run once every three hours in prod
scheduleExpressionMinute = "* * * * *"  # Run once every minute for testing

# Change to your preferred schedule for production
scheduler.add_job(
    main, "cron", minute="*"
)

scheduler.start()
