#!/usr/bin/env python3

from sys import exit
from sgen import generate_startup
from twython import Twython
from credentials import c_key, c_secret, a_token, a_token_secret

# Create a Twython API instance
bot = Twython(c_key, c_secret, a_token, a_token_secret)

# Make sure we are authenticated correctly
try:
    bot.verify_credentials()
except Exception as e:
    print("Authentication Failed", e)
    exit(1)

try:
    status = generate_startup()
    bot.update_status(status=status)
    print('Successfully tweeted "{}".'.format(status))
except Exception as e:
    print("Tweet failed!", e)
    exit(2)
