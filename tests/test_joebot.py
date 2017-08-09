import os

import pytest

from joebot import JoeBot


@pytest.fixture
def joe():
    # starterbot's ID as an environment variable
    SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
    BOT_ID = os.environ.get("BOT_ID")

    # constants
    AT_BOT = "<@" + BOT_ID + ">"
    EXAMPLE_COMMAND = "do"

    joe = JoeBot('starterbot', SLACK_BOT_TOKEN, BOT_ID)
    return joe

def test_connection(joe):
    joe.wake()
    print(JoeBot.rules)